from mysql.connector import connect

connection = connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

cursor = connection.cursor()

query = "update song set duration=%s where id = %s"

values=[3.5,2]

cursor.execute(query,values)

connection.commit()