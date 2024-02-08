from abc import abstractmethod
from typing import Any


class Database:
    db_path: str
    uri: bool
    connection: Any

    @abstractmethod
    def get_cursor(self):
        ...

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def close(self):
        ...
