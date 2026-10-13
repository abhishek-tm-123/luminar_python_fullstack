from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
    
)

cursor = connection.cursor()

query = "update books set price=%s where id = %s"

values=[300,2]

cursor.execute(query,values)

connection.commit()