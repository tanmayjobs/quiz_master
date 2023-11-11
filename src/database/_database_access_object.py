import sqlite3


class DatabaseAccess:
    def __enter__(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect("database/storage/data.sqlite3")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
