from helpers.constants import Errors
from data_containers.user import UserRole, User


def accessed_by(*roles: tuple[UserRole]):

    def wrapper(func):

        def secured_function(self, *args, **kwargs):

            if not isinstance(self.user, User):
                # Here rather than raising error we will send response with performer not send
                raise ValueError(Errors.PERFORMER_REQUIRED)

            if self.user.role not in roles:
                # Here rather than raising error we will send response with permission error
                raise PermissionError(Errors.PERMISSION)

            return func(self, *args, **kwargs)

        return secured_function

    return wrapper
