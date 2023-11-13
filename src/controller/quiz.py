from constants import Strings
from data_containers.quiz import Quiz
from data_containers.types import QuizType
import services.quizs as quizzes
from helpers.rbac import creator_only, admin_only


@creator_only
def add_quiz(quiz: Quiz, **kwargs):
    quizzes.add(quiz)


@creator_only
def get_creator_quizzes(**kwargs):
    creator = kwargs.get(Strings.PERFORMER)
    all_quizzes_data = quizzes.get_by_creator(creator)
    all_quizzes = [Quiz(*quiz, []) for quiz in all_quizzes_data]

    for quiz in all_quizzes:
        types_data = quizzes.get_quiz_types(quiz)
        all_types = [QuizType(*each_type) for each_type in types_data]
        quiz.types = all_types

    return all_quizzes


@admin_only
@creator_only
def remove_quiz(quiz, **kwargs):
    quizzes.remove(quiz)


def all_quiz_types():
    all_types_data = quizzes.all_quiz_types()
    all_types = [QuizType(*each_type) for each_type in all_types_data]

    return all_types
