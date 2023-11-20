import services.quiz as quizzes

from constants import Strings
from data_containers.question import Question
from data_containers.quiz import Quiz
from data_containers.types import QuizType
from data_containers.user import UserRole
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR)
def add_quiz(quiz: Quiz, **_):
    quizzes.add(quiz)


@accessed_by(UserRole.CREATOR)
def get_creator_quizzes(**kwargs):
    creator = kwargs.get(Strings.PERFORMER)

    all_quizzes_data = quizzes.get_by_creator(creator)
    all_quizzes = [Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data]

    return all_quizzes


@accessed_by(UserRole.ADMIN, UserRole.CREATOR)
def remove_quiz(quiz, **_):
    quizzes.remove(quiz)


@accessed_by(UserRole.CREATOR)
def add_question(quiz, question, **_):
    quizzes.add_question(quiz, question)


def get_quiz_questions(quiz):
    questions_data = quizzes.get_quiz_question(quiz)

    questions = [
        Question.parse_json(question_data)
        for question_data in questions_data
    ]

    return questions


def all_quiz_types():
    all_types_data = quizzes.all_quiz_types()
    all_types = [QuizType(*each_type) for each_type in all_types_data]

    return all_types


@accessed_by(UserRole.CREATOR)
def remove_question(question, **_):
    quizzes.remove_question(question)


@accessed_by(UserRole.ADMIN)
def get_all_quizzes(**_):
    all_quizzes_data = quizzes.get_all_quizzes()
    all_quizzes = [Quiz.parse_json(quiz_data) for quiz_data in all_quizzes_data]

    return all_quizzes


def get_random_quiz():
    quiz_data = quizzes.get_random_quiz()

    if not quiz_data:
        return None

    quiz = Quiz.parse_json(quiz_data)
    return quiz


def filter_all_quizzes(search_key):
    all_quizzes_data = quizzes.filter_all_quizzes(search_key)
    all_quizzes = [
        Quiz.parse_json(quiz_data)
        for quiz_data in all_quizzes_data
    ]

    return all_quizzes
