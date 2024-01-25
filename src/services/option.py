import uuid

from pymysql import IntegrityError

from database import MysqlAccess, database
from helpers.constants import SQLQueries
from helpers.exceptions import DoNotExists, NotEnoughPermission


class OptionService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(database)

    def add_option(self, question_id, option_text, is_correct):
        try:
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_OPTION, (uuid.uuid4(), option_text, is_correct, question_id))
        except IntegrityError:
            raise DoNotExists(f"question with question id {question_id} not found!")

    def remove_option(self, option_id, performer_id):
        with self.database_access as dao:
            option = dao.read(SQLQueries.CAN_MODIFY_OPTION, (option_id,), only_one=True)
            if not option:
                raise DoNotExists(f"option with option id {option_id} not found!")
            if option["creator_id"] != performer_id:
                raise NotEnoughPermission
            dao.write(SQLQueries.REMOVE_OPTION, (option_id,))

    def update_option(self, option_id, performer_id, option_text):
        with self.database_access as dao:
            option = dao.read(SQLQueries.CAN_MODIFY_OPTION, (option_id,), only_one=True)
            if not option:
                raise DoNotExists(f"option with option id {option_id} not found!")
            if option["creator_id"] != performer_id:
                raise NotEnoughPermission
            dao.write(SQLQueries.UPDATE_OPTION, (option_text, option_id))
