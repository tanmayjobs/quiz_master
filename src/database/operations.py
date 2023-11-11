from . import _database_access_object as database_access


class LastTransaction:

    def __init__(self, lastrowid, rowcount) -> None:
        self.last_id = lastrowid
        self.rows_changed = rowcount

    @staticmethod
    def from_cursor(cursor):
        return LastTransaction(lastrowid=cursor.lastrowid,
                               rowcount=cursor.rowcount)


def get(query, params, only_one=False):
    with database_access.DatabaseAccess() as dao:
        data = dao.execute(query, params)
        data = data.fetchone() if only_one else data.fetchall()
        return data


def add(query, params):
    with database_access.DatabaseAccess() as dao:
        dao.execute(query, params)
        return LastTransaction.from_cursor(dao)


def remove(query, params):
    with database_access.DatabaseAccess() as dao:
        dao.execute(query, params)


def update(query, params):
    with database_access.DatabaseAccess() as dao:
        dao.execute(query, params)
