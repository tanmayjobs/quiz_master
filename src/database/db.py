import sqlite3

from data_containers.last_transaction import LastTransaction


class Database:
    FILE_PATH = "database/storage/data.sqlite3"

    def __init__(self):
        self.connection = sqlite3.connect(Database.FILE_PATH)
        self.cursor = self.connection.cursor()

    def get(self, query, params=(), only_one=False):
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
