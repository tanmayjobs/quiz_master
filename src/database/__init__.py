"""
Don't import the Database class as long as you don't need a separate instance.
Use the 'database' variable to access the Database class.
"""

import os

from helpers.constants import SQLQueries, Strings, Config
from .db import Database

if os.getcwd().endswith('src'):
    db_path = os.path.dirname(os.path.abspath(__file__)) + Config.SQL_FILE_PATH
    uri = False

    if not os.path.exists(db_path):
        os.mkdir(db_path)

    db_path += f'/{Config.SQL_FILE_NAME}'
else:
    db_path = 'file::memory:?cache=shared'
    uri = True

database = Database(db_path, uri)

database.create(SQLQueries.CREATE_AUTH_TABLE)
database.create(SQLQueries.CREATE_QUIZ_TABLE)
database.create(SQLQueries.CREATE_QUESTION_TABLE)
database.create(SQLQueries.CREATE_OPTION_TABLE)
database.create(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
database.create(SQLQueries.CREATE_TYPE_TABLE)
database.create(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)

database.add(SQLQueries.ADD_TYPE, (Strings.MOVIE,),)
database.add(SQLQueries.ADD_TYPE, (Strings.BOOK,),)
database.add(SQLQueries.ADD_TYPE, (Strings.MUSIC,),)
database.add(SQLQueries.ADD_TYPE, (Strings.OTHER,),)
