import uuid

from pymysql import IntegrityError

from database import MysqlAccess, resource_database
from helpers.constants import SQLQueries, Errors, Strings
from helpers.exceptions import DoNotExists, NotEnoughPermission


class OptionService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(resource_database)

    def add_option(self, question_id, option_text, is_correct):
        try:
            with self.database_access as dao:
                dao.write(
                    SQLQueries.ADD_OPTION,
                    (uuid.uuid4(), option_text, is_correct, question_id),
                )
        except IntegrityError:
            raise DoNotExists(Errors.QUESTION_NOT_FOUND.format(id=question_id))

    def remove_option(self, option_id, performer_id):
        with self.database_access as dao:
            option = dao.read(SQLQueries.CAN_MODIFY_OPTION, (option_id,), only_one=True)
            if not option:
                raise DoNotExists(Errors.OPTION_NOT_FOUND.format(id=option_id))
            if option[Strings.CREATOR_ID] != performer_id:
                raise NotEnoughPermission(Errors.NOT_CREATOR_OF_QUIZ)
            dao.write(SQLQueries.REMOVE_OPTION, (option_id,))

    def update_option(self, option_id, performer_id, option_text, is_correct):
        with self.database_access as dao:
            option = dao.read(SQLQueries.CAN_MODIFY_OPTION, (option_id,), only_one=True)
            if not option:
                raise DoNotExists(Errors.OPTION_NOT_FOUND.format(id=option_id))
            if option[Strings.CREATOR_ID] != performer_id:
                raise NotEnoughPermission(Errors.NOT_CREATOR_OF_QUIZ)
            dao.write(SQLQueries.UPDATE_OPTION, (option_text, is_correct, option_id))
