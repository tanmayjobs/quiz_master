from database.last_transaction import LastTransaction
from database.database_access import DatabaseAccess
from helpers.constants import LogText
from helpers.log import logger


class SqliteAccess(DatabaseAccess):
    def __enter__(self):
        self.cursor = self.database.connection.cursor()
        return self

    def __exit__(self, *error_details):
        if not any(error_details):
            self.database.connection.commit()
        else:
            self.database.connection.rollback()
            logger.warn(LogText.SYSTEM_ERROR)

    def read(self, query, params=(), only_one=False):
        self.cursor.execute(query, params)
        return self.cursor.fetchone() if only_one else self.cursor.fetchall()

    def write(self, query, params=()):
        self.cursor.execute(query, params)
        return LastTransaction.from_cursor(self.cursor)

    def write_many(self, query, *params):
        self.cursor.executemany(query, params)