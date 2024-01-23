import uuid

from pymysql import IntegrityError

from database import MysqlAccess, database
from helpers.constants import SQLQueries
from helpers.exceptions import DoNotExists, AlreadyExists


class QuizService:

    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(database)

    def add_quiz(self, quiz_name, creator_id, tags):
        try:
            quiz_id = uuid.uuid4()
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_QUIZ, (quiz_id, quiz_name, creator_id))
                for tag_id in tags:
                    dao.write(SQLQueries.ADD_QUIZ_TYPE, (uuid.uuid4(), quiz_id, tag_id,),)

        except IntegrityError as error:
            if "quiz_name" in error.args[1]:
                raise AlreadyExists(409, "Conflict", f"quiz with name {quiz_name} already exists!")
            raise DoNotExists(404, "Not Found", "one or more tag ids are invalid!")

    def remove_quiz(self, quiz_id, creator_id):
        try:
            with self.database_access as dao:
                last_transaction = dao.write(SQLQueries.REMOVE_QUIZ, (quiz_id, creator_id))
                if not last_transaction.rows_changed:
                    raise IntegrityError
        except IntegrityError:
            raise DoNotExists(404, "Not Found", f"quiz with quiz id {quiz_id} not found!")

    def add_tag(self, quiz_id, tag_id):
        ...

    def remove_tag(self, quiz_id, tag_id):
        ...
