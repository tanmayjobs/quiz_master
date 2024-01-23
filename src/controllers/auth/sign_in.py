from schemas import SignInResponse
from utils.tokens import generate_token
from helpers.exceptions import CustomException
from services.auth import AuthServices


class SignInController:
    def __init__(self, json_data, auth_service=None):
        self.username = json_data["username"]
        self.password = json_data["password"]
        self.auth_service = auth_service or AuthServices()

    def __call__(self):
        try:
            user = self.auth_service.sign_in(self.username, self.password)
            access_token = generate_token(user)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"access_token": access_token}, 200
