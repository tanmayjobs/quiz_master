import uuid

from database import MysqlAccess
from helpers.constants import SQLQueries


class RecordService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess()

    def get_records(self, args):
        with self.database_access as dao:
            filters = [key + " = %s" for key in args.keys()]
            if filters:
                where_clause = ", ".join(filters)
            else:
                where_clause = "1 = 1"
            query = SQLQueries.GET_RECORDS.format(where_clause)
            records = dao.read(query, tuple(args.values()))
        return records

    def add_record(self, quiz_id, user_id, score):
        with self.database_access as dao:
            dao.write(SQLQueries.ADD_SCORE, (uuid.uuid4(), quiz_id, user_id, score))
