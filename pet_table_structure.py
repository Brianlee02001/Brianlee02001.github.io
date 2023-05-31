import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)
cursor = conn.cursor()

query = "DESCRIBE pet"
cursor.execute(query)

columns = cursor.fetchall()

for column in columns:
    print(column)

cursor.close()
conn.close()
