from flask_jwt_extended import get_jwt, get_jwt_identity

from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import logger
from services.tokens import TokenService
from utils.rbac import validate_token_details


@validate_token_details(
    UserRole.PLAYER.value, UserRole.ADMIN.value, UserRole.CREATOR.value, refresh=True
)
class RefreshTokenController:
    def __init__(self, token_service=None):
        self.user_id = get_jwt_identity()
        self.jwt = get_jwt()
        self.token_service = token_service or TokenService()

    def __call__(self):
        try:
            tokens_json = self.token_service.refresh_access_token(
                self.user_id, self.jwt
            )
        except CustomException as custom_error:
            logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return tokens_json, HTTPStatuses.OK.code
