from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.question import QuestionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value, UserRole.PLAYER.value)
class GetQuestionController:
    def __init__(self, question_id, question_service=None):
        self.question_id = question_id
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            question = self.question_service.get_question(self.question_id)
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return question, HTTPStatuses.OK.code
