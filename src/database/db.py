import sqlite3


class Database:
    """
    This class creates a database connection based on the path provided.
    Don't create objects of this class unnecessarily, see the __init__.py file of database package.
    """

    def __init__(self, db_path, uri):
        self.db_path = db_path
        self.uri = uri
        self.connection = sqlite3.connect(db_path, uri=uri)

    def __del__(self):
        self.connection.close()
