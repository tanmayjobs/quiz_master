from abc import ABC, abstractmethod

from .mysql.mysql_db import MySQLDatabase


class DatabaseAccess(ABC):
    """
    To perform any operation on the database a context manager is required.
    The context manager provides the CRUD operations for the database, check __init__.py of database package for more.
    """

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(self, *error_details):
        ...

    @abstractmethod
    def read(self, query, params=(), only_one=False):
        ...

    @abstractmethod
    def write(self, query, params=()):
        ...
