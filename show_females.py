import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
    database="menagerie"
)
c = conn.cursor()
def show_female_dogs():
    c.execute("SELECT * FROM pet WHERE sex='f'")
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    show_female_dogs()


if __name__ == '__main__':
    main()