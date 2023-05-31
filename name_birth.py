import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)

cursor = conn.cursor()

query = "SELECT name, birth FROM pet"
cursor.execute(query)

rows = cursor.fetchall()

print("Name and Birth columns from the pet table:")
for row in rows:
    name = row[0]
    birth = row[1]
    print(f"Name: {name}, Birth: {birth}")

cursor.close()
conn.close()
