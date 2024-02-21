"""
This file is responsible to create the required folders for storing database file.
And also responsible to create the database.
Don't use _create_database_folder and _init_database functions outside this module.

IMPORTANT: Don't import the Database class as long as you don't need a separate instance.
IMPORTANT: Use the 'database' variable to access the Database object.

Example:
    from database import database, DatabaseAccess
    with DatabaseAccess(database) as dao:
        database_access_object.read(...)
        database_access_object.write(...)
        ...

"""

from .mysql.mysql_access import MysqlAccess
from .mysql.mysql_db import MySQLDatabase
from .sqlite.sqlite_db import SqliteDatabase
from helpers.constants import SQLQueries
from .database_access import DatabaseAccess
from .db import Database
from .sqlite.sqlite_access import SqliteAccess


def _init_resource_database(database_access):
    with database_access as dao:
        dao.write(SQLQueries.CREATE_AUTH_TABLE)
        dao.write(SQLQueries.CREATE_QUIZ_TABLE)
        dao.write(SQLQueries.CREATE_QUESTION_TABLE)
        dao.write(SQLQueries.CREATE_OPTION_TABLE)
        dao.write(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
        dao.write(SQLQueries.CREATE_TYPE_TABLE)
        dao.write(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)


def _init_token_database(database_access):
    with database_access as dao:
        dao.write(SQLQueries.CREATE_TOKEN_TABLE)


def init_db(app):
    with app.app_context():
        _init_resource_database(MysqlAccess())
        _init_token_database(MysqlAccess())
