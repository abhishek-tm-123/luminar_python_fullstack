from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost"
    
)

cursor = connection.cursor()

query = "create database book_db"

cursor.execute(query)