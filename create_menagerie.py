import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Valorantjett123')
c = conn.cursor()


def createdb():
    c.execute("CREATE DATABASE menagerie")


def main():
    createdb()


if __name__ == '__main__':
    main()