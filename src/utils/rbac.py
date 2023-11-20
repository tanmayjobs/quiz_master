from constants import Errors, Strings
from data_containers.user import UserRole


def accessed_by(*roles: tuple[UserRole]):
    def wrapper(func):
        def secured_function(*args, **kwargs):

            performer = kwargs.get(Strings.PERFORMER)

            if not performer:
                # Here rather than raising error we will send response with performer not send
                raise ValueError(Errors.PERFORMER_REQUIRED)

            if performer.role not in roles:
                # Here rather than raising error we will send response with permission error
                raise PermissionError(Errors.PERMISSION)

            return func(*args, **kwargs)

        return secured_function

    return wrapper
