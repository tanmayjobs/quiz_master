from data_containers.last_transaction import LastTransaction
from database import Database


class DBContext:

    def __init__(self, database: Database):
        self.database = database

    def __enter__(self):
        self.cursor = self.database.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database.connection.commit()

    def get(self, query, params=(), only_one=False):
        data = self.cursor.execute(query, params)
        data = data.fetchone() if only_one else data.fetchall()

        return data

    def add(self, query, params=()):
        self.cursor.execute(query, params)
        return LastTransaction.from_cursor(self.cursor)

    def remove(self, query, params=()):
        self.cursor.execute(query, params)

    def update(self, query, params=()):
        self.cursor.execute(query, params)

    def create(self, query, params=()):
        self.cursor.execute(query, params)
