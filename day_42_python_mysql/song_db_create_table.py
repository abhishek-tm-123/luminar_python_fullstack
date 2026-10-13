from mysql.connector import connect

connection = connect(
    user="root",
    password = "Password@123",
    host="localhost",
    database="song_db"
)

cursor = connection.cursor()

query = """

create table song(
    id int auto_increment primary key,
    title varchar(200) not null,
    singers varchar(200) not null,
    track_num int not null,
    duration float
)

"""

cursor.execute(query)
