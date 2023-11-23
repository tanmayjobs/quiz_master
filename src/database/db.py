import os
import sqlite3

from data_containers.last_transaction import LastTransaction
from helpers.log.logger import Logger, DEBUG


class Database:

    def __init__(self, db_path, uri):
        Logger.log(DEBUG, db_path)
        self.db_path = db_path
        self.uri = uri
        self.connection = sqlite3.connect(db_path, uri=uri)

    def __del__(self):
        self.connection.close()
