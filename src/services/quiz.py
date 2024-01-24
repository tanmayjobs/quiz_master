import json
import uuid

from pymysql import IntegrityError

from database import MysqlAccess, database
from helpers.constants import SQLQueries
from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import DoNotExists, AlreadyExists, NotEnoughPermission


class QuizService:

    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(database)

    def get_quizzes(self):
        with self.database_access as dao:
            quizzes_data = dao.read(SQLQueries.GET_ALL_QUIZZES)
        return [{**quiz_data, "tags": json.loads(f"[{quiz_data['tags']}]"), "questions": json.loads(quiz_data["questions"] or "[]")} for quiz_data in quizzes_data]

    def get_quiz(self, quiz_id):
        with self.database_access as dao:
            quiz_data = dao.read(SQLQueries.GET_QUIZ, (quiz_id,), only_one=True)
        if not quiz_data:
            raise DoNotExists(HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, f"quiz with quiz id {quiz_id} not found!")
        return {**quiz_data, "tags": json.loads(f"[{quiz_data['tags']}]"), "questions": json.loads(quiz_data["questions"] or "[]")}

    def add_quiz(self, quiz_name, creator_id, tags, questions):
        try:
            quiz_id = uuid.uuid4()
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_QUIZ, (quiz_id, quiz_name, creator_id, json.dumps(questions)))
                for tag_id in tags:
                    dao.write(SQLQueries.ADD_QUIZ_TYPE, (uuid.uuid4(), quiz_id, tag_id))
        except IntegrityError as error:
            if "quiz_name" in error.args[1]:
                raise AlreadyExists(HTTPStatuses.CONFLICT.code, HTTPStatuses.CONFLICT.status, f"quiz with name {quiz_name} already exists!")
            raise DoNotExists(HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, f"tag with tag id {tag_id} not found!")

    def remove_quiz(self, quiz_id, user_id, is_admin):
        with self.database_access as dao:
            quiz = dao.read(SQLQueries.GET_QUIZ_BY_ID, (quiz_id,), only_one=True)
            if not quiz:
                raise DoNotExists(HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, f"quiz with quiz id {quiz_id} not found!")
            if not is_admin and not quiz["creator_id"] == user_id:
                raise NotEnoughPermission(HTTPStatuses.FORBIDDEN.code, HTTPStatuses.FORBIDDEN.status, "you don't have enough permission to modify this quiz!")
            dao.write(SQLQueries.REMOVE_QUIZ, (quiz_id, user_id))

    def add_tag(self, quiz_id, tag_id):
        try:
            with self.database_access as dao:
                dao.write(SQLQueries.ADD_QUIZ_TYPE, (uuid, quiz_id, tag_id))
        except IntegrityError as error:
            if "quiz_id" in error.args[1]:
                raise DoNotExists(HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, f"quiz with quiz id {quiz_id} not found!")
            raise DoNotExists(HTTPStatuses.NOT_FOUND.code, HTTPStatuses.NOT_FOUND.status, f"tag with tag id {tag_id} not found!")

    def remove_tag(self, quiz_id, tag_id):
        with self.database_access as dao:
            dao.write(SQLQueries.REMOVE_QUIZ_TYPE, (quiz_id, tag_id))
