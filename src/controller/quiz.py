from helpers.constants import Strings, SQLQueries
from data_containers.quiz import Quiz
from data_containers.types import QuizType
from data_containers.user import UserRole
from database import database
from utils.rbac import accessed_by


class QuizHandler:

    def __init__(self, user, quiz=None):
        self.user = user    # User whose trying to perform the operation
        self.quiz = quiz    # Quiz on which the operations are performed

    @accessed_by(UserRole.CREATOR)
    def add_quiz(self):
        quiz_id = database.add(SQLQueries.ADD_QUIZ, (self.quiz.creator_id, self.quiz.quiz_name))
        quiz_id = quiz_id.last_id

        for quiz_type in self.quiz.types:
            database.add(SQLQueries.ADD_QUIZ_TYPE, (quiz_id, quiz_type.type_id,))

    @staticmethod
    def get_random_quiz():
        quiz_data = database.get(SQLQueries.GET_RANDOM_QUIZ, only_one=True)

        if not quiz_data:
            return None
        quiz = Quiz.parse_json(quiz_data)

        return quiz

    @accessed_by(UserRole.CREATOR)
    def get_user_quizzes(self):
        all_quizzes_data = database.get(SQLQueries.GET_USER_QUIZZES, (self.user.user_id,))
        all_quizzes = [Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data]

        return all_quizzes

    @accessed_by(UserRole.ADMIN)
    def get_all_quizzes(self):
        all_quizzes_data = database.get(SQLQueries.GET_ALL_QUIZZES)
        all_quizzes = [Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data]

        return all_quizzes

    @staticmethod
    def filter_all_quizzes(search_key):
        all_quizzes_data = database.get(
            SQLQueries.FILTER_ALL_QUIZZES, (
                Strings.FILTER.format(search_key=search_key),
                Strings.FILTER.format(search_key=search_key),
            )
        )

        all_quizzes = [
            Quiz.parse_json(quiz_data)
            for quiz_data in all_quizzes_data
        ]

        return all_quizzes

    @accessed_by(UserRole.ADMIN, UserRole.CREATOR)
    def remove_quiz(self):
        if not self.quiz:
            raise ValueError
        database.remove(SQLQueries.REMOVE_QUIZ, (self.quiz.quiz_id,))

    @staticmethod
    def defined_quiz_types():
        all_types_data = database.get(SQLQueries.GET_ALL_TYPES)
        all_types = [QuizType(*each_type) for each_type in all_types_data]

        return all_types
