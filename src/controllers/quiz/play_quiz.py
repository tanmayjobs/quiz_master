from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.enum.user_role import UserRole
from services.play import PlayService
from services.question import QuestionService
from services.record import RecordService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.PLAYER.value)
class PlayQuizController:
    def __init__(self, json_data, question_service=None, play_service=None, record_service=None):
        self.quiz_id = json_data[Strings.QUIZ_ID]
        self.answers = json_data[Strings.ANSWERS]
        self.user_id = get_jwt_identity()
        self.question_service = question_service or QuestionService()
        self.play_service = play_service or PlayService()
        self.record_service = record_service or RecordService()

    def __call__(self):
        questions = self.question_service.get_questions(self.quiz_id, UserRole.CREATOR.value)
        total_score = self.play_service.play(questions, self.answers)
        self.record_service.add_record(self.quiz_id, self.user_id, total_score)

        return {
            Strings.QUIZ_ID: self.quiz_id,
            Strings.USER_ID: self.user_id,
            Strings.SCORE: total_score
        }, 201
