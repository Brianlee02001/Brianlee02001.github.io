import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Valorantjett123')
c = conn.cursor()


def show_databases():
    databases = ("show databases")
    c.execute(databases)
    for databases in c:
        print(databases[0])


def commit_close():
    conn.commit()
    c.close()
    conn.close()


def main():
    show_databases()
    commit_close()


if __name__ == '__main__':
    main()