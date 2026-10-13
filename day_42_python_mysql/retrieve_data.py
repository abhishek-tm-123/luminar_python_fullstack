from mysql.connector import connect

connection = connect(
    user="root",
    password = "Password@123",
    host = "localhost",
    database="song_db"
    
)

cursor = connection.cursor()

query = """

select * from song where id = %s

"""

values=[1]

cursor.execute(query,values)

record = cursor.fetchone()

print(record)
