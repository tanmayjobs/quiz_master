from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.option import OptionService
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR.value)
class AddOptionController:
    def __init__(self, quiz_id, json_data, option_service=None):
        self.performer_id = get_jwt_identity()
        self.quiz_id = quiz_id
        self.question_text = json_data["question_text"]
        self.options = json_data["options"]
        self.option_service = option_service or OptionService()

    def __call__(self):
        try:
            self.option_service.add_option(self.quiz_id, self.question_text, self.options)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"result": "created"}, 201
