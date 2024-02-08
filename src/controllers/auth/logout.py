from flask_jwt_extended import get_jwt, get_jwt_identity

from helpers.constants import Strings, LogText
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from utils.rbac import validate_token_details
from services.tokens import TokenService


@validate_token_details(
    UserRole.PLAYER.value, UserRole.ADMIN.value, UserRole.CREATOR.value
)
class LogoutController:
    def __init__(self, token_service=None):
        jwt = get_jwt()
        self.token_pair_id = jwt[Strings.TOKEN_PAIR_ID]
        self.user_id = get_jwt_identity()
        self.exp = jwt[Strings.EXP]
        self.token_service = token_service or TokenService()

    def __call__(self):
        try:
            self.token_service.invalidate_token_pair(
                self.token_pair_id, self.user_id, self.exp
            )
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.LOGOUT}, HTTPStatuses.OK.code
