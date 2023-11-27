import sqlite3

from helpers.log.logger import Logger, DEBUG


class Database:
    """
    This class creates a database connection based on the path provided.
    Don't create objects of this class unnecessarily, see the __init__.py file of database package.
    """

    def __init__(self, db_path, uri):
        Logger.log(DEBUG, db_path)
        self.db_path = db_path
        self.uri = uri
        self.connection = sqlite3.connect(db_path, uri=uri)

    def __del__(self):
        self.connection.close()
