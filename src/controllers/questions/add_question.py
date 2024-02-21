from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.question import QuestionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value)
class AddQuestionController:
    def __init__(self, quiz_id, json_data, question_service=None):
        self.performer_id = get_jwt_identity()
        self.quiz_id = quiz_id
        self.question_text = json_data[Strings.QUESTION_TEXT]
        self.options = json_data[Strings.OPTIONS]
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            question_id = self.question_service.add_question(
                self.quiz_id, self.question_text, self.options
            )
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.CREATED, Strings.QUESTION_ID: question_id}, HTTPStatuses.CREATED.code
