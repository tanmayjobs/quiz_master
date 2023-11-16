import database.operations as database
from constants import SQLQueries
from data_containers.quiz import Quiz
from data_containers.quiz_record import QuizRecord
from data_containers.user import User


def get_player_scores(player: User):
    return database.get(SQLQueries.GET_PLAYER_SCORES, (player.user_id,))


def quiz_top_scores(quiz_id: str, number_of_scores: int):
    return database.get(SQLQueries.TOP_QUIZ_SCORES, (quiz_id, number_of_scores))


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
