from .sqlite_db import SqliteDatabase
from ..database_access import DatabaseAccess
from ..last_transaction import LastTransaction


class SqliteAccess(DatabaseAccess):

    def __init__(self):
        self.database = SqliteDatabase()

    def __enter__(self):
        self.database.connect()
        self.cursor = self.database.get_cursor()
        return self

    def __exit__(self, *error_details):
        self.database.close()

    def read(self, query, params=(), only_one=False):
        self.cursor.execute(query, params)
        return self.cursor.fetchone() if only_one else self.cursor.fetchall()

    def write(self, query, params=()):
        self.cursor.execute(query, params)
        return LastTransaction.from_cursor(self.cursor)

    def write_many(self, query, *params):
        self.cursor.executemany(query, params)
