import uuid

from pymysql import IntegrityError

from database import MysqlAccess, database
from helpers.constants import SQLQueries
from helpers.exceptions import DoNotExists, NotEnoughPermission


class QuestionService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(database)

    def add_question(self, quiz_id, question_text, options):
        try:
            with self.database_access as dao:
                question_id = uuid.uuid4()
                dao.write(SQLQueries.ADD_QUESTION, (question_id, quiz_id, question_text))
                for option in options:
                    dao.write(
                        SQLQueries.ADD_OPTION,
                        (question_id, option["option_text"], option["is_correct"]),
                    )
        except IntegrityError:
            raise DoNotExists(f"quiz with quiz id {quiz_id} not found!")

    def remove_question(self, performer_id, question_id):
        with self.database_access as dao:
            question = dao.read(SQLQueries.GET_QUESTION_BY_ID, (question_id,), only_one=True)
            if not question:
                raise DoNotExists(f"question with question id {question_id} not found!")
            if question["creator_id"] != performer_id:
                raise NotEnoughPermission(403, "Forbidden", "you don't have enough permissions!")
            dao.write(SQLQueries.REMOVE_QUESTION, (question_id,))

    def update_question(self, performer_id, question_id):
        with self.database_access as dao:
            question = dao.read(SQLQueries.GET_QUESTION_BY_ID, (question_id,), only_one=True)
            if not question:
                raise DoNotExists(f"question with question id {question_id} not found!")
            if question["creator_id"] != performer_id:
                raise NotEnoughPermission(403, "Forbidden", "you don't have enough permissions!")
            dao.write(SQLQueries.REMOVE_QUESTION, (question_id,))

