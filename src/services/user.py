from database import MysqlAccess
from helpers.constants import SQLQueries, Errors
from helpers.exceptions import DoNotExists


class UserServices:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess()

    def get_users(self):
        with self.database_access as dao:
            users = dao.read(SQLQueries.GET_USERS, )
        return users

    def remove_user(self, user_id):
        with self.database_access as dao:
            user = dao.read(SQLQueries.GET_USER_BY_ID, (user_id,), only_one=True)
            if not user:
                raise DoNotExists(Errors.USER_NOT_FOUND.format(id=user_id))
            dao.write(SQLQueries.REMOVE_USER, (user_id,))
