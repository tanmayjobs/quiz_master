import os

from constants import SQLQueries, Strings
from . import _database_access_object as database_access

if not os.path.exists("database/storage/"):
    os.mkdir("database/storage/")

with database_access.DatabaseAccess() as dao:
    dao.execute(SQLQueries.CREATE_AUTH_TABLE)
    dao.execute(SQLQueries.CREATE_QUIZ_TABLE)
    dao.execute(SQLQueries.CREATE_QUESTION_TABLE)
    dao.execute(SQLQueries.CREATE_OPTION_TABLE)
    dao.execute(SQLQueries.CREATE_QUIZ_SCORE_TABLE)
    dao.execute(SQLQueries.CREATE_TYPE_TABLE)
    dao.execute(SQLQueries.CREATE_QUIZ_TYPE_MAPPING_TABLE)

    dao.executemany(
        SQLQueries.ADD_TYPE,
        [
            (Strings.MOVIE,),
            (Strings.MUSIC,),
            (Strings.BOOK,)
        ]
    )

__all__ = ['operations']
