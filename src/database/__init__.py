"""
Don't import the Database class as long as you don't need a separate instance.
Use the 'database' variable to access the Database class and it's functionalities.
"""

import os

from helpers.constants import SQLQueries, Strings, Config
from .db import Database
from .db_context import DBContext

db_path = None
uri = False
database = None


def create_folder():
    global db_path, uri
    db_path = os.path.dirname(os.path.abspath(__file__)) + Config.SQL_FILE_PATH
    uri = False
    if not os.path.exists(db_path):
        os.mkdir(db_path)
    db_path += f'/{Config.SQL_FILE_NAME}'


def create_database():
    global db_path, uri, database
    database = Database(db_path, uri)
    with DBContext(database) as dao:
        dao.create(SQLQueries.CREATE_AUTH_TABLE)
        dao.create(SQLQueries.CREATE_QUIZ_TABLE)
        dao.create(SQLQueries.CREATE_QUESTION_TABLE)
        dao.create(SQLQueries.CREATE_OPTION_TABLE)
        dao.create(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
        dao.create(SQLQueries.CREATE_TYPE_TABLE)
        dao.create(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)

        dao.add(
            SQLQueries.ADD_TYPE,
            (Strings.MOVIE,),
        )
        dao.add(
            SQLQueries.ADD_TYPE,
            (Strings.BOOK,),
        )
        dao.add(
            SQLQueries.ADD_TYPE,
            (Strings.MUSIC,),
        )
        dao.add(
            SQLQueries.ADD_TYPE,
            (Strings.OTHER,),
        )


create_folder()
create_database()
