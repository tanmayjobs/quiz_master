import os

from helpers.constants import SQLQueries, Strings
from .db import Database

if not os.path.exists("database/storage/"):
    os.mkdir("database/storage/")

database = Database()

database.create(SQLQueries.CREATE_AUTH_TABLE)
database.create(SQLQueries.CREATE_QUIZ_TABLE)
database.create(SQLQueries.CREATE_QUESTION_TABLE)
database.create(SQLQueries.CREATE_OPTION_TABLE)
database.create(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
database.create(SQLQueries.CREATE_TYPE_TABLE)
database.create(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)

database.add(SQLQueries.ADD_TYPE,(Strings.MOVIE,),)
database.add(SQLQueries.ADD_TYPE,(Strings.BOOK,),)
database.add(SQLQueries.ADD_TYPE,(Strings.MUSIC,),)
database.add(SQLQueries.ADD_TYPE,(Strings.OTHER,),)
