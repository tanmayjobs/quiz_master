from database import SqliteDatabase
from database.last_transaction import LastTransaction
from database.database_access import DatabaseAccess
from helpers.constants import LogText
from helpers.log import request_logger


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
