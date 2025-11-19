from getpass import getpass
from werkzeug.security import generate_password_hash
from db import get_db
from dotenv import load_dotenv
load_dotenv()

def main():
    username = input("Admin username: ").strip()
    if not username:
        print("Username required"); return
    password = getpass("Admin passoword: ").strip()
    if not password:
        print("Password required"); return
    pw_hash = generate_password_hash(password)
    conn = get_db()
    if not conn:
        print("DB connection failed"); return
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password_hash, role) VALUES (%s,%s,%s)",(username, pw_hash, "admin"))
        conn.commit()
        print("Admin created:", username)
    except Exception as e:
        conn.rollback()
        print("ERROR:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()

