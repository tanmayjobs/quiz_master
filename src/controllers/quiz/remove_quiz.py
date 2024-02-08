from flask_jwt_extended import get_jwt_identity, get_jwt

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.quiz import QuizService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.ADMIN.value, UserRole.CREATOR.value)
class RemoveQuizController:
    def __init__(self, quiz_id, quiz_service=None):
        self.performer_id = get_jwt_identity()
        self.role = get_jwt()[Strings.ROLE]
        self.quiz_id = quiz_id
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            self.quiz_service.remove_quiz(
                self.quiz_id, self.performer_id, self.role == UserRole.ADMIN
            )
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.REMOVED}, HTTPStatuses.OK.code
