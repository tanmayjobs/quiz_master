from pymysql.cursors import DictCursor
import pymysql
import os
import dotenv


dotenv.load_dotenv()


class Database:
    """
    This class creates a database connection based on the path provided.
    Don't create objects of this class unnecessarily, see the __init__.py file of database package.
    """

    def __init__(self, db_path=None, uri=None):
        self.db_path = db_path
        self.uri = uri
        self.connection = pymysql.connect(
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME"),
            cursorclass=DictCursor,
        )

    def __del__(self):
        self.connection.close()
