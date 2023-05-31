import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Valorantjett123",
)
c = conn.cursor()
def dropdb():
    c.execute("DROP DATABASE IF EXISTS menagerie")


def main():
    dropdb()


if __name__ == '__main__':
    main()