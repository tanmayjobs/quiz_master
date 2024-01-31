from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.option import OptionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value)
class RemoveOptionController:
    def __init__(self, option_id, option_service=None):
        self.performer_id = get_jwt_identity()
        self.option_id = option_id
        self.option_service = option_service or OptionService()

    def __call__(self):
        try:
            self.option_service.remove_option(self.option_id, self.performer_id)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.REMOVED}, HTTPStatuses.OK.code
