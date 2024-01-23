from helpers.exceptions import CustomException
from services.auth import AuthServices


class SignUpController:
    def __init__(self, json_data, auth_service=None):
        self.username = json_data["username"]
        self.password = json_data["password"]
        self.auth_service = auth_service or AuthServices()

    def __call__(self):
        try:
            self.auth_service.sign_up(self.username, self.password)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"created": "ok"}, 200
