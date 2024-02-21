import os

import dotenv
import pymysql
from flask import current_app
from pymysql.cursors import DictCursor

from ..db import Database

dotenv.load_dotenv()


class MySQLDatabase(Database):
    """
    This class creates a database connection based on the path provided.
    Don't create objects of this class unnecessarily, see the __init__.py file of database package.
    """

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=os.getenv("DATABASE_HOST"),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                database=os.getenv("DATABASE_NAME"),
                cursorclass=DictCursor,
            )
        except pymysql.Error as error:
            current_app.logger.error(error)
            raise

    def get_cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()
