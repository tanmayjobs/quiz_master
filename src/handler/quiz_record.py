from data_containers.quiz_record import QuizRecord
from database import database, DBContext
from helpers.constants import SQLQueries


class QuizRecordHandler:
    """
    This handler deals with quiz records.
    Doesn't require any parameters as it have only static methods.
    Implements add record, get top record, get all records of a user.
    """

    @staticmethod
    def add_quiz_record(quiz_record):
        with DBContext(database) as dao:
            dao.write(
                SQLQueries.ADD_QUIZ_SCORE,
                (
                    quiz_record.player_id,
                    quiz_record.quiz_id,
                    quiz_record.player_score,
                    quiz_record.total_score,
                ),
            )

    @staticmethod
    def get_user_records(user):
        with DBContext(database) as dao:
            player_scores_data = dao.read(SQLQueries.GET_PLAYER_SCORES, (user.user_id,))
        player_scores = [QuizRecord(*score_data) for score_data in player_scores_data]

        return player_scores

    @staticmethod
    def quiz_top_records(quiz_id, number_of_records=5):
        with DBContext(database) as dao:
            top_records_data = dao.read(
                SQLQueries.TOP_QUIZ_SCORES, (quiz_id, number_of_records)
            )
        top_records = [QuizRecord(*score_data) for score_data in top_records_data]

        return top_records
