import json
import uuid

from pymysql import IntegrityError

from database import MysqlAccess
from helpers.constants import SQLQueries, Strings, Errors
from helpers.exceptions import DoNotExists, AlreadyExists, NotEnoughPermission


class QuizService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess()

    def get_quizzes(self):
        with self.database_access as dao:
            quizzes_data = dao.read(SQLQueries.GET_ALL_QUIZZES)
        return [
            {**quiz_data, Strings.TAGS: json.loads(f"[{quiz_data[Strings.TAGS]}]")}
            for quiz_data in quizzes_data
        ]

    def get_quiz(self, quiz_id):
        with self.database_access as dao:
            quiz_data = dao.read(SQLQueries.GET_QUIZ, (quiz_id,), only_one=True)
        if not quiz_data:
            raise DoNotExists(Errors.QUIZ_NOT_FOUND.format(id=quiz_id))
        return {**quiz_data, Strings.TAGS: json.loads(f"[{quiz_data[Strings.TAGS]}]")}

    def add_quiz(self, quiz_name, creator_id, tags):
        try:
            quiz_id = uuid.uuid4()
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_QUIZ, (quiz_id, quiz_name, creator_id))
                for tag_id in tags:
                    dao.write(SQLQueries.ADD_QUIZ_TAG, (uuid.uuid4(), quiz_id, tag_id))
        except IntegrityError as error:
            if Strings.QUIZ_NAME in error.args[1]:
                raise AlreadyExists(Errors.QUIZ_ALREADY_EXISTS.format(quiz_name))
            raise DoNotExists(Errors.TAG_NOT_FOUND.format(id=tag_id))

    def remove_quiz(self, quiz_id, user_id, is_admin):
        with self.database_access as dao:
            quiz = dao.read(SQLQueries.GET_QUIZ_BY_ID, (quiz_id,), only_one=True)
            if not quiz:
                raise DoNotExists(Errors.QUIZ_NOT_FOUND.format(id=quiz_id))
            if not is_admin and not quiz[Strings.CREATOR_ID] == user_id:
                raise NotEnoughPermission()
            dao.write(SQLQueries.REMOVE_QUIZ, (quiz_id, user_id))
