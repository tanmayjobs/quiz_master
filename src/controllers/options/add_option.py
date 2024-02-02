from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import logger
from services.option import OptionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value)
class AddOptionController:
    def __init__(self, question_id, json_data, option_service=None):
        self.performer_id = get_jwt_identity()
        self.question_id = question_id
        self.option_text = json_data[Strings.OPTION_TEXT]
        self.is_correct = json_data[Strings.IS_CORRECT]
        self.option_service = option_service or OptionService()

    def __call__(self):
        try:
            self.option_service.add_option(
                self.question_id, self.option_text, self.is_correct
            )
        except CustomException as custom_error:
            logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.CREATED}, HTTPStatuses.CREATED.code
