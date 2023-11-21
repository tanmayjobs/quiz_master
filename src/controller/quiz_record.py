from helpers.constants import SQLQueries
from data_containers.quiz_record import QuizRecord
from database import database


class QuizRecordHandler:

    @staticmethod
    def add_quiz_record(quiz_record):
        database.add(
            SQLQueries.ADD_QUIZ_SCORE,
            (
                quiz_record.player_id,
                quiz_record.quiz_id,
                quiz_record.player_score,
                quiz_record.total_score
            )
        )

    @staticmethod
    def get_user_records(user):
        player_scores_data = database.get(SQLQueries.GET_PLAYER_SCORES, (user.user_id,))
        player_scores = [QuizRecord(*score_data) for score_data in player_scores_data]

        return player_scores

    @staticmethod
    def quiz_top_records(quiz_id, number_of_records=5):
        top_records_data = database.get(SQLQueries.TOP_QUIZ_SCORES, (quiz_id, number_of_records))
        top_records = [QuizRecord(*score_data) for score_data in top_records_data]

        return top_records
