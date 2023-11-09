import sqlite3
import os

from src.helpers.constants import SQLQueries

class DatabaseAccess:
    def __enter__(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect("src/database/data.db")
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


class Database:
    def __init__(self):
        if not os.path.exists("src/database/"):
            os.mkdir("src/database/")

        with DatabaseAccess() as dao:
            dao.execute(SQLQueries.CREATE_AUTH_TABLE)
            dao.execute(SQLQueries.CREATE_QUIZ_TABLE)
            dao.execute(SQLQueries.CREATE_QUESTION_TABLE)
            dao.execute(SQLQueries.CREATE_OPTION_TABLE)
            dao.execute(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
            dao.execute(SQLQueries.CREATE_TYPE_TABLE)
            dao.execute(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)
