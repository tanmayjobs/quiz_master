from constants import Errors, Strings
from data_containers.user import UserRole


def accessed_by(*roles: tuple[UserRole]):
    def wrapper(func):
        def secured_function(*args, **kwargs):
            performer = kwargs.get(Strings.PERFORMER)

            if not performer:
                raise ValueError(Errors.PERFORMER_REQUIRED)

            if performer.role not in roles:
                raise PermissionError(Errors.PERMISSION)

            return func(*args, **kwargs)

        return secured_function

    return wrapper
