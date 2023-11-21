class LastTransaction:

    def __init__(self, last_id, rows_changed) -> None:
        self.last_id = last_id
        self.rows_changed = rows_changed

    @staticmethod
    def from_cursor(cursor):
        return LastTransaction(
            last_id=cursor.lastrowid,
            rows_changed=cursor.rowcount
        )
