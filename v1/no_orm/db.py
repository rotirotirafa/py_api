#!/usr/bin/python
import psycopg2

from config import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD, DB_PORT


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        # create a cursor
        cursor = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# if __name__ == '__main__':
#     connect()
#

class DatabaseConnection:

    def __init__(self, conn=None, cursor=None):
        self.conn = None
        self.cursor = self.connect()

    def connect(self):
        self.conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        return self.conn.cursor()

    def exec_test(self):
        # execute a statement
        print('PostgreSQL database version:')
        self.cursor.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = self.cursor.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        self.cursor.close()
        return db_version


a = DatabaseConnection()

if __name__ == '__main__':
    a = DatabaseConnection()
    a.exec_test()
