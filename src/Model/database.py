import sqlite3

class Database:
    def __init__(self):
        self.db_name = 'diagnostics.db'

    def connect(self):
        return sqlite3.connect(self.db_name)

    def close(self, conn):
        conn.close()

    def execute_query(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()
        self.close(conn)

    def execute_select(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        self.close(conn)
        return result
