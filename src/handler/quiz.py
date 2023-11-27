from data_containers.quiz import Quiz
from data_containers.types import QuizType
from data_containers.user import UserRole
from database import database, DBContext
from helpers.constants import Strings, SQLQueries
from utils.rbac import accessed_by


class QuizHandler:
    """
    This handler requires a user and a quiz as parameters.
        user:   User is required in every case as quiz is an important entity of our system,
                so it's important to know which user want to access the quiz functionalities.

        quiz:   Quiz is required in adding, removing otherwise it will be None by default.
    This handler implements add, get, remove and filter quizzes.
    """

    def __init__(self, user, quiz=None):
        self.user = user  # User whose trying to perform the operation
        self.quiz = quiz  # Quiz on which the operations are performed

    @accessed_by(UserRole.CREATOR)
    def add_quiz(self):
        if not self.quiz:
            raise ValueError

        with DBContext(database) as dao:
            quiz_id = dao.write(SQLQueries.ADD_QUIZ,
                                (self.user.user_id, self.quiz.quiz_name))
            quiz_id = quiz_id.last_id

            for quiz_type in self.quiz.types:
                dao.write(SQLQueries.ADD_QUIZ_TYPE, (
                    quiz_id,
                    quiz_type.type_id,
                ))

    @staticmethod
    def get_random_quiz():
        with DBContext(database) as dao:
            quiz_data = dao.read(SQLQueries.GET_RANDOM_QUIZ, only_one=True)

        if not quiz_data:
            return None

        quiz = Quiz.parse_json(quiz_data)
        return quiz

    @accessed_by(UserRole.CREATOR)
    def get_user_quizzes(self):
        with DBContext(database) as dao:
            all_quizzes_data = dao.read(SQLQueries.GET_USER_QUIZZES,
                                        (self.user.user_id,))
        all_quizzes = [
            Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data
        ]

        return all_quizzes

    @accessed_by(UserRole.ADMIN)
    def get_all_quizzes(self):
        with DBContext(database) as dao:
            all_quizzes_data = dao.read(SQLQueries.GET_ALL_QUIZZES)
        all_quizzes = [
            Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data
        ]

        return all_quizzes

    @staticmethod
    def filter_all_quizzes(search_key):
        with DBContext(database) as dao:
            all_quizzes_data = dao.read(SQLQueries.FILTER_ALL_QUIZZES, (
                Strings.FILTER.format(search_key=search_key),
                Strings.FILTER.format(search_key=search_key),
            ))

        all_quizzes = [
            Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data
        ]

        return all_quizzes

    @accessed_by(UserRole.ADMIN, UserRole.CREATOR)
    def remove_quiz(self):
        if not self.quiz:
            raise ValueError

        with DBContext(database) as dao:
            dao.write(SQLQueries.REMOVE_QUIZ, (self.quiz.quiz_id,))

    @staticmethod
    def defined_quiz_types():
        with DBContext(database) as dao:
            all_types_data = dao.read(SQLQueries.GET_ALL_TYPES)
        all_types = [QuizType(*each_type) for each_type in all_types_data]

        return all_types
