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

    def connect(self):
        self.connection = sqlite3.connect(
            self.db_path or os.getenv("TOKEN_DATABASE"),
            uri=self.uri,
            check_same_thread=False
        )

    def get_cursor(self):
        return self.connection.cursor()

    def close(self, commit=True):
        self.connection.commit() if commit else self.connection.rollback()
        self.connection.close()
