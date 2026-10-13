from mysql.connector import connect

connection = connect(
    user="root",
    password = "Password@123",
    host="localhost"
)

print(connection)