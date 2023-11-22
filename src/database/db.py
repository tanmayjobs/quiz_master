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
        self.cursor = self.connection.cursor()

    def get(self, query, params=(), only_one=False):
        data = self.cursor.execute(query, params)
        data = data.fetchone() if only_one else data.fetchall()

        return data

    def add(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

        return LastTransaction.from_cursor(self.cursor)

    def remove(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def update(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def create(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
