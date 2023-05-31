import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)

cursor = conn.cursor()

query = "SELECT * FROM pet"
cursor.execute(query)

rows = cursor.fetchall()

print("Records from the pet table:")
for row in rows:
    print(row)

cursor.close()
conn.close()
