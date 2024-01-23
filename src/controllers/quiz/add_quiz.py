from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.quiz import QuizService
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR.name)
class AddQuizController:
    def __init__(self, json_data, quiz_service=None):
        self.performer_id = get_jwt_identity()
        self.quiz_name = json_data["quiz_name"]
        self.tags = json_data["tags"]
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            self.quiz_service.add_quiz(self.quiz_name, self.performer_id, self.tags)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"created": "ok"}, 201
