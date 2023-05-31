import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)

cursor = conn.cursor()

query = """
SELECT owner, COUNT(*) as num_pets
FROM pet
GROUP BY owner
"""
cursor.execute(query)

rows = cursor.fetchall()

print("Number of pets per owner:")
for row in rows:
    owner = row[0]
    num_pets = row[1]
    print(f"{owner}: {num_pets} pet(s)")

cursor.close()
conn.close()