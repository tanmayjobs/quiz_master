import database.operations as database
from constants import SQLQueries
from data_containers.types import QuizType

from data_containers.user import UserRole
from data_containers.quiz import Quiz


def get_by_creator(user) -> list['Quiz']:
    if user.role != UserRole.CREATOR:
        raise PermissionError

    ...  # Get quizzes by creator.


def get_all_quizzes(user) -> list[Quiz]:
    if user.role != UserRole.ADMIN:
        raise PermissionError

    ...  # Get all quizzes.
    return []


def add(quiz: Quiz) -> None:

    quiz_id = database.add(SQLQueries.ADD_QUIZ, (quiz.creator_id, quiz.quiz_name))
    quiz_id = quiz_id.last_id

    for quiz_type in quiz.types:
        database.add(SQLQueries.ADD_QUIZ_TYPE, (quiz_id, quiz_type.type_id,))


def remove(self, user) -> None:
    if self.creator_id != user.user_id and user.role != UserRole.ADMIN:
        raise PermissionError

    ...  # Remove the quiz from the database.


def all_quiz_types() -> list:
    all_types = database.get(SQLQueries.GET_ALL_TYPES)
    return all_types
