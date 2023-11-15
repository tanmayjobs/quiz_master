import services.quiz_records as quiz_records
from constants import Strings
from data_containers.quiz_record import QuizRecord
from data_containers.user import UserRole
from helpers.rbac import accessed_by


def add_quiz_record(quiz_record):
    quiz_records.add(quiz_record)


@accessed_by(UserRole.PLAYER, UserRole.CREATOR)
def get_player_records(**kwargs):
    player = kwargs.get(Strings.PERFORMER)

    player_scores_data = quiz_records.get_player_scores(player)
    player_scores = [QuizRecord(*score_data) for score_data in player_scores_data]

    return player_scores
