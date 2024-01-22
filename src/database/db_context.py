from data_containers.last_transaction import LastTransaction
from database import Database
from helpers.constants import LogText
from helpers.log import logger


class DBContext:
    """
    To perform any operation on the database a context manager is required.
    The context manager provides the CRUD operations for the database, check __init__.py of database package for more.
    """

    def __init__(self, database: Database):
        self.database = database

    def __enter__(self):
        self.cursor = self.database.connection.cursor()
        return self

    def __exit__(self, *error_details):
        if not any(error_details):
            self.database.connection.commit()
        else:
            logger.warn(LogText.SYSTEM_ERROR)

    def read(self, query, params=(), only_one=False):
        self.cursor.execute(query, params)
        return self.cursor.fetchone() if only_one else self.cursor.fetchall()

    def write(self, query, params=()):
        self.cursor.execute(query, params)
        return LastTransaction.from_cursor(self.cursor)
