import database.operations as database
from constants import SQLQueries

from data_containers.user import UserRole
from data_containers.quiz import Quiz


def get_by_creator(user) -> list:
    quizzes = database.get(SQLQueries.GET_QUIZZES_BY_CREATOR, (user.user_id,))
    return quizzes


def get_quiz_types(quiz):
    all_types = database.get(SQLQueries.GET_QUIZ_TYPES, (quiz.quiz_id,))
    return all_types


def add(quiz: Quiz) -> None:

    quiz_id = database.add(SQLQueries.ADD_QUIZ, (quiz.creator_id, quiz.quiz_name))
    quiz_id = quiz_id.last_id

    for quiz_type in quiz.types:
        database.add(SQLQueries.ADD_QUIZ_TYPE, (quiz_id, quiz_type.type_id,))


def remove(quiz) -> None:
    database.remove(SQLQueries.REMOVE_QUIZ, (quiz.quiz_id,))


def all_quiz_types() -> list:
    all_types = database.get(SQLQueries.GET_ALL_TYPES)
    return all_types


def add_question(quiz, question):
    question_id = database.add(SQLQueries.ADD_QUESTION, (quiz.quiz_id, question.question_text))
    question_id = question_id.last_id

    for option in question.options:
        database.add(SQLQueries.ADD_OPTION, (question_id, option.option_text, option.is_correct))


def remove_question(question):
    database.remove(SQLQueries.REMOVE_OPTION_BY_QUESTION, (question.question_id,))
    database.remove(SQLQueries.REMOVE_QUESTION, (question.question_id,))


def get_quiz_question(quiz):
    return database.get(SQLQueries.GET_QUIZ_QUESTIONS, (quiz.quiz_id,))


def get_all_quizzes():
    return database.get(SQLQueries.GET_ALL_QUIZZES)


def filter_all_quizzes(search_key):
    return database.get(
        SQLQueries.FILTER_ALL_QUIZZES, (
            search_key,
            search_key
        )
    )


def get_random_quiz():
    return database.get(SQLQueries.GET_RANDOM_QUIZ, only_one=True)