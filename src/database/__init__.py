"""
This file is responsible to create the required folders for storing database file.
And also responsible to create the databases.

IMPORTANT: Don't import the Database class as long as you don't need a separate instance.
IMPORTANT: Use the 'database' variable to access the Database object.

Example:
    from database import database, DBContext
    with DBContext(database) as database_access_object:
        database_access_object.add(...)
        database_access_object.remove(...)
        ...

"""

import os

from helpers.constants import SQLQueries, Strings, Config
from .db import Database
from .db_context import DBContext

db_path = os.path.dirname(os.path.abspath(__file__)) + Config.SQL_FILE_PATH
uri = False
if not os.path.exists(db_path):
    os.mkdir(db_path)
db_path += f'/{Config.SQL_FILE_NAME}'


database = Database(db_path, uri)
with DBContext(database) as dao:
    dao.write(SQLQueries.CREATE_AUTH_TABLE)
    dao.write(SQLQueries.CREATE_QUIZ_TABLE)
    dao.write(SQLQueries.CREATE_QUESTION_TABLE)
    dao.write(SQLQueries.CREATE_OPTION_TABLE)
    dao.write(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
    dao.write(SQLQueries.CREATE_TYPE_TABLE)
    dao.write(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)

    dao.write(
        SQLQueries.ADD_TYPE,
        (Strings.MOVIE,),
    )
    dao.write(
        SQLQueries.ADD_TYPE,
        (Strings.BOOK,),
    )
    dao.write(
        SQLQueries.ADD_TYPE,
        (Strings.MUSIC,),
    )
    dao.write(
        SQLQueries.ADD_TYPE,
        (Strings.OTHER,),
    )
