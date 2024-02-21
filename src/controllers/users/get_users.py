from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.user import UserServices


class GetUsersController:
    def __init__(self, user_service=None):
        self.user_service = user_service or UserServices()

    def __call__(self):
        try:
            users = self.user_service.get_users()
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.USERS: users}, 200
