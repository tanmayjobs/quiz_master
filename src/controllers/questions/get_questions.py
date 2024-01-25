from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.question import QuestionService
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR.value)
class GetQuestionsController:
    def __init__(self, quiz_id, question_service=None):
        self.quiz_id = quiz_id
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            questions = self.question_service.get_questions(self.quiz_id)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"questions": questions}, 201
