from db import get_db
import hashlib

username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter role (admin/user): ")

hashed = hashlib.sha256(password.encode()).hexdigest()

db = get_db()
cursor = db.cursor()
cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", (username, hashed, role))
db.commit()
print(f"User '{username}' created successfully.")
cursor.close()
db.close()


