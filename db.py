import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
	user="adminweb",
	password="19122006",
	database="adminpanel"
    )
