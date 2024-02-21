from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.quiz import QuizService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value)
class AddQuizController:
    def __init__(self, json_data, quiz_service=None):
        self.performer_id = get_jwt_identity()
        self.quiz_name = json_data[Strings.QUIZ_NAME]
        self.tags = json_data[Strings.TAG_IDS]
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            quiz_id = self.quiz_service.add_quiz(self.quiz_name, self.performer_id, self.tags)
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.CREATED, Strings.QUIZ_ID: quiz_id}, HTTPStatuses.CREATED.code
