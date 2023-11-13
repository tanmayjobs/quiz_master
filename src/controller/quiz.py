from constants import Strings
from data_containers.quiz import Quiz
from data_containers.types import QuizType
from data_containers.user import User, UserRole
import services.quizs as quizzes
from helpers.rbac import creator_only


@creator_only
def add_quiz(quiz: Quiz, **kwargs):
    quizzes.add(quiz)


def all_quiz_types():
    all_types_data = quizzes.all_quiz_types()
    all_types = [QuizType(*each_type) for each_type in all_types_data]

    return all_types
