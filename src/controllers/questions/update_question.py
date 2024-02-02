from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import logger
from services.question import QuestionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value)
class UpdateQuestionController:
    def __init__(self, question_id, json_data, question_service=None):
        self.performer_id = get_jwt_identity()
        self.question_id = question_id
        self.question_text = json_data[Strings.QUESTION_TEXT]
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            self.question_service.update_question(
                self.performer_id, self.question_id, self.question_text
            )
        except CustomException as custom_error:
            logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.UPDATED}, HTTPStatuses.OK.code
