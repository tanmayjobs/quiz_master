import database.operations as database
from constants import SQLQueries
from data_containers.quiz_record import QuizRecord


def get_by_user_id(user_id):
    ...  # Get user's all quiz records.


def get_by_quiz_id(quiz_id):
    ...  # Get all records for a quiz.


def add(quiz_record: QuizRecord):
    database.add(
        SQLQueries.ADD_QUIZ_SCORE,
        (
            quiz_record.player_id,
            quiz_record.quiz_id,
            quiz_record.player_score,
            quiz_record.total_score
        )
    )
