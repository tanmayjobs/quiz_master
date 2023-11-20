import sqlite3


class LastTransaction:

    def __init__(self, lastrowid, rowcount) -> None:
        self.last_id = lastrowid
        self.rows_changed = rowcount

    @staticmethod
    def from_cursor(cursor):
        return LastTransaction(
            lastrowid=cursor.lastrowid,
            rowcount=cursor.rowcount
        )


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database/storage/data.sqlite3")
        self.cursor = self.connection.cursor()

    def get(self, query, params=tuple(), only_one=False):
        data = self.cursor.execute(query, params)
        data = data.fetchone() if only_one else data.fetchall()

        return data

    def add(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()
        return LastTransaction.from_cursor(self.cursor)

    def remove(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def update(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def create(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
