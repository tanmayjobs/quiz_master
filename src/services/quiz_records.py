import database.operations as database
from constants import SQLQueries
from data_containers.quiz_record import QuizRecord
from data_containers.user import User


def get_player_scores(player: User):
    return database.get(SQLQueries.GET_PLAYER_SCORES, (player.user_id,))


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
