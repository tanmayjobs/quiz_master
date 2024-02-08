from flask import current_app

from database import MySQLDatabase
from database.last_transaction import LastTransaction
from database.database_access import DatabaseAccess
from helpers.constants import LogText
from helpers.log import request_logger


class MysqlAccess(DatabaseAccess):
    """
    To perform any operation on the database a context manager is required.
    The context manager provides the CRUD operations for the database, check __init__.py of database package for more.
    """

    def __init__(self):
        self.database = MySQLDatabase()

    def __enter__(self):
        self.database.connect()
        self.cursor = self.database.get_cursor()
        return self

    def __exit__(self, *error_details):
        if not any(error_details):
            self.database.connection.commit()
        else:
            self.database.connection.rollback()
            current_app.logger.warning(LogText.SYSTEM_ERROR)
            request_logger.warning(LogText.SYSTEM_ERROR)
        self.database.close()

    def read(self, query, params=(), only_one=False):
        self.cursor.execute(query, params)
        return self.cursor.fetchone() if only_one else self.cursor.fetchall()

    def write(self, query, params=()):
        self.cursor.execute(query, params)
        return LastTransaction.from_cursor(self.cursor)
