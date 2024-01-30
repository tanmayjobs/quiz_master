from flask_jwt_extended import get_jwt_identity

from helpers.constants import Strings
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.user import UserServices
from utils.rbac import accessed_by


@accessed_by(UserRole.ADMIN.value)
class RemoveUserController:
    def __init__(self, user_id, user_service=None):
        self.performer_id = get_jwt_identity()
        self.user_id = user_id
        self.user_service = user_service or UserServices()

    def __call__(self):
        try:
            self.user_service.remove_user(self.user_id)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.REMOVED}, 200
