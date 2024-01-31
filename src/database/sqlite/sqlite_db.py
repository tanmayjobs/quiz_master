from pymysql.cursors import DictCursor
import sqlite3
import os
import dotenv

from ..db import Database

dotenv.load_dotenv()


class SqliteDatabase(Database):

    def __init__(self, db_path=None, uri=False):
        self.db_path = db_path
        self.uri = uri
        self.connection = sqlite3.connect(
            db_path or os.getenv("TOKEN_DATABASE"),
            uri,
            check_same_thread=False
        )

    def __del__(self):
        self.connection.close()
