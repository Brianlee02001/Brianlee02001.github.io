import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)

cursor = conn.cursor()

query = """
SELECT name, birth, MONTH(birth) AS month_birth
FROM pet
"""
cursor.execute(query)

rows = cursor.fetchall()

print("Name, Birth, and Month(Birth) columns from the pet table:")
for row in rows:
    name = row[0]
    birth = row[1]
    month_birth = row[2]
    print(f"Name: {name}, Birth: {birth}, Month(Birth): {month_birth}")

cursor.close()
conn.close()
