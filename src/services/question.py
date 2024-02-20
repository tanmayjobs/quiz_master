import json
import uuid

from pymysql import IntegrityError

from database import MysqlAccess
from helpers.constants import SQLQueries, Errors, Strings
from helpers.enum.user_role import UserRole
from helpers.exceptions import DoNotExists, NotEnoughPermission


class QuestionService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess()

    def get_questions(self, quiz_id, user_role):
        with self.database_access as dao:
            quiz = dao.read(SQLQueries.GET_QUIZ_BY_ID, (quiz_id,), only_one=True)
            if not quiz:
                raise DoNotExists(Errors.QUIZ_NOT_FOUND.format(id=quiz_id))

            get_questions_query = (
                SQLQueries.GET_QUESTIONS_AS_PLAYER
                if user_role == UserRole.PLAYER.value
                else SQLQueries.GET_QUESTIONS_AS_CREATOR
            )

            questions = dao.read(get_questions_query, (quiz_id,))
        return [
            {**question, Strings.OPTIONS: json.loads(f"[{question[Strings.OPTIONS]}]")}
            for question in questions
        ]

    def get_question(self, question_id):
        with self.database_access as dao:
            question = dao.read(
                SQLQueries.GET_QUIZ_QUESTION, (question_id,), only_one=True
            )
        if not question:
            raise DoNotExists(Errors.QUESTION_NOT_FOUND.format(id=question_id))
        question = {
            **question,
            Strings.OPTIONS: json.loads(f"[{question[Strings.OPTIONS]}]"),
        }
        return question

    def add_question(self, quiz_id, question_text, options):
        try:
            with self.database_access as dao:
                question_id = uuid.uuid4()
                dao.write(
                    SQLQueries.ADD_QUESTION, (question_id, question_text, quiz_id)
                )
                for option in options:
                    dao.write(
                        SQLQueries.ADD_OPTION,
                        (
                            uuid.uuid4(),
                            option[Strings.OPTION_TEXT],
                            option[Strings.IS_CORRECT],
                            question_id,
                        ),
                    )
        except IntegrityError as error:
            print(error)
            raise DoNotExists(Errors.QUIZ_NOT_FOUND.format(id=quiz_id))

    def remove_question(self, performer_id, question_id):
        with self.database_access as dao:
            question = dao.read(
                SQLQueries.GET_QUESTION_BY_ID, (question_id,), only_one=True
            )
            if not question:
                raise DoNotExists(Errors.QUESTION_NOT_FOUND.format(id=question_id))
            if question[Strings.CREATOR_ID] != performer_id:
                raise NotEnoughPermission()
            dao.write(SQLQueries.REMOVE_QUESTION, (question_id,))

    def update_question(self, performer_id, question_id, question_text):
        with self.database_access as dao:
            question = dao.read(
                SQLQueries.GET_QUESTION_BY_ID, (question_id,), only_one=True
            )
            if not question:
                raise DoNotExists(Errors.QUESTION_NOT_FOUND.format(id=question_id))
            if question[Strings.CREATOR_ID] != performer_id:
                raise NotEnoughPermission()
            dao.write(
                SQLQueries.UPDATE_QUESTION,
                (
                    question_text,
                    question_id,
                ),
            )
