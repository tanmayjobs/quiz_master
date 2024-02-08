from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.quiz import QuizService
from utils.rbac import validate_token_details


class GetQuizzesController:
    def __init__(self, quiz_service=None):
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            quizzes = self.quiz_service.get_quizzes()
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.QUIZZES: quizzes}, HTTPStatuses.OK.code
