import services.quiz as quizzes
import json

from constants import Strings, Numbers
from data_containers.question import Option, Question
from data_containers.quiz import Quiz
from data_containers.types import QuizType
from helpers.rbac import creator_only, admin_only


@creator_only
def add_quiz(quiz: Quiz, **_):
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
def remove_quiz(quiz, **_):
    quizzes.remove(quiz)


@creator_only
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

        question_text = question_data[Strings.QUESTION_TEXT]
        option_json = json.loads(Strings.ARRAY.format(question_data[Strings.OPTIONS_JSON]))
        options = _map_options(option_json)

        question = Question(
            question_text,
            options
        )
        questions.append(question)

    return questions


def all_quiz_types():
    all_types_data = quizzes.all_quiz_types()
    all_types = [QuizType(*each_type) for each_type in all_types_data]

    return all_types
