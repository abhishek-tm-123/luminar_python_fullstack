from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query="""
insert into books(title,auther,price,pages) values
(%s,%s,%s,%s)
"""

values=['Harry Potter', 'J. K. Rowling', 599.00, 400]

cursor.execute(query,values)

connection.commit()