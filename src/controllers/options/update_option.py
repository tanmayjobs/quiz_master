from flask_jwt_extended import get_jwt_identity

from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.option import OptionService
from utils.rbac import accessed_by


@accessed_by(UserRole.CREATOR.value)
class UpdateOptionController:
    def __init__(self, option_id, json_data, option_service=None):
        self.performer_id = get_jwt_identity()
        self.option_id = option_id
        self.option_text = json_data["option_text"]
        self.is_correct = json_data["is_correct"]
        self.option_service = option_service or OptionService()

    def __call__(self):
        try:
            self.option_service.update_option(self.option_id, self.performer_id, self.option_text, self.is_correct)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"result": "update"}, 200
