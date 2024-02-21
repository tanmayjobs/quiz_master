from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.auth import AuthServices


class SignUpController:
    def __init__(self, json_data, auth_service=None):
        self.username = json_data[Strings.USERNAME]
        self.password = json_data[Strings.PASSWORD]
        self.auth_service = auth_service or AuthServices()

    def __call__(self):
        try:
            user_id = self.auth_service.sign_up(self.username, self.password)
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.CREATED, Strings.USER_ID: user_id}, HTTPStatuses.CREATED.code