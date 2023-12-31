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

    def read(self, query, params=(), only_one=False):
        logger.info(LogText.READING_DATA)
        data = self.cursor.execute(query, params)
        data = data.fetchone() if only_one else data.fetchall()

        return data

    def write(self, query, params=()):
        logger.info(LogText.WRITING_DATA)
        self.cursor.execute(query, params)

        return LastTransaction.from_cursor(self.cursor)
