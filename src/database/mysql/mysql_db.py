from pymysql.cursors import DictCursor
import pymysql
import os
import dotenv
from ..db import Database


dotenv.load_dotenv()


# def singleton_db():
#     database = pymysql.connect(
#         host=os.getenv("DATABASE_HOST"),
#         user=os.getenv("DATABASE_USER"),
#         password=os.getenv("DATABASE_PASSWORD"),
#         database=os.getenv("DATABASE_NAME"),
#         cursorclass=DictCursor,
#     )
#     while True:
#         yield database


class MySQLDatabase(Database):
    """
    This class creates a database connection based on the path provided.
    Don't create objects of this class unnecessarily, see the __init__.py file of database package.
    """
    def __init__(self, db_path=None, uri=None):
        self.db_path = db_path
        self.uri = uri
        self.database = ...  # or singleton_db()

    def connect(self):
        self.connection = next(self.database)

    def get_cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()
