import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host":os.environ.get("DB_HOST"),
    "user":os.environ.get("DB_USER"),
    "pasword":os.environ.get("DB_PASSWORD"),
    "database":os.environ.get("DB_NAME"),
}

def get_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print("DB connection error", e)
        return None
