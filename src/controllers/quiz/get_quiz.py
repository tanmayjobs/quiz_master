from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.quiz import QuizService
from utils.rbac import accessed_by


class GetQuizController:
    def __init__(self, quiz_id, quiz_service=None):
        self.quiz_id = quiz_id
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            quiz = self.quiz_service.get_quiz(self.quiz_id)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return quiz, 200
