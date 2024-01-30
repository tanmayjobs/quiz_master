from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from utils.tokens import generate_token
from helpers.exceptions import CustomException
from services.auth import AuthServices


class SignInController:
    def __init__(self, json_data, auth_service=None):
        self.username = json_data[Strings.USERNAME]
        self.password = json_data[Strings.PASSWORD]
        self.auth_service = auth_service or AuthServices()

    def __call__(self):
        try:
            user = self.auth_service.sign_in(self.username, self.password)
            access_token = generate_token(user)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.ACCESS_TOKEN: access_token}, HTTPStatuses.OK.code
