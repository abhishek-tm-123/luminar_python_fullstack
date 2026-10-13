from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
    
)

cursor = connection.cursor()

query = "select * from books"

cursor.execute(query)

records = cursor.fetchall()

for r in records:
    print(r)