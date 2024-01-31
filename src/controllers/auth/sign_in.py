from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import CustomException
from services.auth import AuthServices
from services.tokens import TokenService


class SignInController:
    def __init__(self, json_data, auth_service=None, token_service=None):
        self.username = json_data[Strings.USERNAME]
        self.password = json_data[Strings.PASSWORD]
        self.auth_service = auth_service or AuthServices()
        self.token_service = token_service or TokenService()

    def __call__(self):
        try:
            user = self.auth_service.sign_in(self.username, self.password)
            tokens_json = self.token_service.generate_tokens(user, fresh=True)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return tokens_json, HTTPStatuses.OK.code
