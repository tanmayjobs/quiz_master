from flask_jwt_extended import get_jwt_identity, get_jwt

from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.question import QuestionService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.CREATOR.value, UserRole.PLAYER.value)
class GetQuestionsController:
    def __init__(self, quiz_id, question_service=None):
        self.quiz_id = quiz_id
        self.user_role = get_jwt()[Strings.ROLE]
        self.question_service = question_service or QuestionService()

    def __call__(self):
        try:
            questions = self.question_service.get_questions(
                self.quiz_id, self.user_role
            )
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.QUESTIONS: questions}, HTTPStatuses.OK.code
