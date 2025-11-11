# app.py
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash
from db import get_db
import os

app = Flask(__name__)

# secret key for session management
app.secret_key = os.environ.get("SECRET_KEY", "dev_key_please_change")

@app.route('/')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    role = session.get('role', 'user')
    return f"""
    <h1>Velkommen {session['username']}!</h1>
    <p>Rolle: {role}</p>
    <a href='/logout'>Logg ut</a>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT password_hash, role FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()
        db.close()

        if user and check_password_hash(user[0], password):
            session['username'] = username
            session['role'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            error = "Feil brukernavn eller passord"

    # if GET request or login failed
    return """
    <form method='POST'>
        <h2>Server Admin Panel Login</h2>
        <label>Brukernavn:</label><br>
        <input type='text' name='username' required><br>
        <label>Passord:</label><br>
        <input type='password' name='password' required><br><br>
        <button type='submit'>Logg inn</button>
        <p style='color:red;'>{}</p>
    </form>
    """.format(error or "")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
