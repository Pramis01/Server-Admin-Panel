
# app.py
from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db
from dotenv import load_dotenv
import os

load_dotenv()  # sørger for at .env lastes

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret_change_me")  # må være satt i .env i prod

# Hjelpefunksjoner
def create_user(username: str, password: str, role: str = "user"):
    pw_hash = generate_password_hash(password)
    conn = get_db()
    if not conn:
        return False, "DB-tilkobling feilet"
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
            (username, pw_hash, role)
        )
        conn.commit()
        return True, None
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        cur.close()
        conn.close()

def find_user_by_username(username: str):
    conn = get_db()
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, username, password_hash, role FROM users WHERE username=%s", (username,))
        row = cur.fetchone()
        return row  # None eller (id, username, pw_hash, role)
    finally:
        cur.close()
        conn.close()

# Ruter
@app.route("/", methods=["GET"])
def index():
    # Hvis bruker er logget inn -> redirect til dashboard
    if session.get("username"):
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    role = request.form.get("role", "user").strip()

    if not username or not password or role not in ("user", "admin"):
        return render_template("index.html", register_error="Fyll ut alle felt riktig")

    ok, err = create_user(username, password, role)
    if not ok:
        # typisk feilmelding: Duplicate entry for username
        return render_template("index.html", register_error=f"Kunne ikke opprette bruker: {err}")
    return render_template("index.html", login_error="Bruker opprettet — logg inn nå")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username or not password:
        return render_template("index.html", login_error="Fyll ut bruker og passord")

    row = find_user_by_username(username)
    if row and check_password_hash(row[2], password):
        session["user_id"] = row[0]
        session["username"] = row[1]
        session["role"] = row[3]
        return redirect(url_for("dashboard"))
    return render_template("index.html", login_error="Feil brukernavn eller passord")

@app.route("/dashboard")
def dashboard():
    if not session.get("username"):
        return redirect(url_for("index"))
    # Eksempelvis hent servers for brukeren (kan utvides)
    return render_template("dashboard.html", username=session.get("username"), role=session.get("role"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
<<<<<<< HEAD

=======
>>>>>>> 804a26e (legg til)
