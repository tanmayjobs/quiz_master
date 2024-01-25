from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.question import QuestionService
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR.value)
class UpdateQuestionController:
    def __init__(self, question_id, json_data, question_service=None):
        self.performer_id = get_jwt_identity()
        self.question_id = question_id
        self.question_text = json_data["question_text"]
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            self.question_service.update_question(self.performer_id, self.question_id, self.question_text)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"result": "updated"}, 201
