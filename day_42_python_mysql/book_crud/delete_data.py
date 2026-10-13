from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
    
)

cursor = connection.cursor()

query = "delete from books where id=%s"

values=[5]

cursor.execute(query,values)

connection.commit()