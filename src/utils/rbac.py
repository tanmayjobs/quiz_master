from flask_jwt_extended import verify_jwt_in_request, get_jwt
from helpers.exceptions import NotEnoughPermission


def accessed_by(*roles: str):
    def wrapper(cls):
        init = cls.__init__

        def secured_init(self, *args, **kwargs):
            verify_jwt_in_request()
            role = get_jwt()["role"]
            if role not in roles:
                raise NotEnoughPermission(403, "Forbidden", "you don't have enough permissions!")
            return init(self, *args, **kwargs)

        cls.__init__ = secured_init
        return cls

    return wrapper
