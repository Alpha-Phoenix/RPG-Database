import psycopg2


def main():
    try:
        connect_str = "dbname='rpgdb' user='bcc321' host='localhost' " + \
                      "password='bcc321-17.2'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # run a SELECT statement - no data in there, but we can try it
        cursor.execute("""SELECT * FROM rpg.item""")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Cannot connect to database")
        print(e)
    pass


if __name__ == '__main__':
    main()
