import services.quiz as quizzes
import json

from constants import Strings, Numbers
from data_containers.question import Option, Question
from data_containers.quiz import Quiz
from data_containers.types import QuizType
from data_containers.user import UserRole
from helpers.rbac import accessed_by


@accessed_by(UserRole.CREATOR)
def add_quiz(quiz: Quiz, **_):
    quizzes.add(quiz)


@accessed_by(UserRole.CREATOR)
def get_creator_quizzes(**kwargs):
    creator = kwargs.get(Strings.PERFORMER)
    all_quizzes_data = quizzes.get_by_creator(creator)
    all_quizzes = _map_quizzes(all_quizzes_data)

    return all_quizzes


@accessed_by(UserRole.ADMIN, UserRole.CREATOR)
def remove_quiz(quiz, **_):
    quizzes.remove(quiz)


@accessed_by(UserRole.CREATOR)
def add_question(quiz, question, **_):
    quizzes.add_question(quiz, question)


def _map_options(options_json):
    options = []

    for option_data in options_json:
        option = Option(
            option_text=option_data[Strings.OPTION.lower()],
            is_correct=option_data[Strings.IS_CORRECT],
        )
        options.append(option)

    return options


def get_quiz_questions(quiz):
    questions_data = quizzes.get_quiz_question(quiz)
    questions = []

    for question_data in questions_data:

        question_id = question_data[Numbers.ZERO]
        question_text = question_data[Strings.QUESTION_TEXT]
        option_json = json.loads(Strings.ARRAY.format(question_data[Strings.OPTIONS_JSON]))
        options = _map_options(option_json)

        question = Question(
            question_id,
            question_text,
            options
        )
        questions.append(question)

    return questions


def all_quiz_types():
    all_types_data = quizzes.all_quiz_types()
    all_types = [QuizType(*each_type) for each_type in all_types_data]

    return all_types


@accessed_by(UserRole.CREATOR)
def remove_question(question, **_):
    quizzes.remove_question(question)


def _get_types(types_json):
    types = []

    for type_json in types_json:
        each_type = QuizType(
            type_json[Strings.TYPE_ID],
            type_json[Strings.TYPE_NAME]
        )

        types.append(each_type)

    return types


def _map_quiz(quiz_data):
    quiz_id, quiz_name, creator_id, creator_name, types = quiz_data
    types = Strings.ARRAY.format(types)
    types_json = json.loads(types)

    types = _get_types(types_json)

    quiz = Quiz(quiz_id, quiz_name, creator_id, creator_name, types)
    return quiz


def _map_quizzes(all_quizzes_data):
    all_quizzes = []

    for quiz_data in all_quizzes_data:
        quiz = _map_quiz(quiz_data)
        all_quizzes.append(quiz)

    return all_quizzes


@accessed_by(UserRole.ADMIN)
def get_all_quizzes(**_):
    all_quizzes_data = quizzes.get_all_quizzes()
    all_quizzes = _map_quizzes(all_quizzes_data)

    return all_quizzes


def get_random_quiz():
    quiz_data = quizzes.get_random_quiz()

    if not quiz_data:
        return None

    quiz = _map_quiz(quiz_data)
    return quiz
