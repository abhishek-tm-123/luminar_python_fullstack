from mysql.connector import connect

connection = connect(
    user="root",
    password = "Password@123",
    host="localhost",
    database="expense_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM expense_tracker")

# Display column names
for column in cursor.column_names:
    print(column, end=" | ")

print()

# Display records
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()