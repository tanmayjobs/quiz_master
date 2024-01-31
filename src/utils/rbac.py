from flask_jwt_extended import verify_jwt_in_request, get_jwt

from helpers.log import logger
from services.tokens import TokenService
from helpers.constants import Strings, LogText
from helpers.exceptions import NotEnoughPermission, BlockedToken


def validate_token_details(*roles: str, check_fresh=False, refresh=False):
    def wrapper(cls):
        init = cls.__init__

        def secured_init(self, *args, **kwargs):
            verify_jwt_in_request(
                fresh=check_fresh,
                refresh=refresh,
                verify_type=True
            )

            jwt = get_jwt()
            token_pair_id = jwt[Strings.TOKEN_PAIR_ID]
            if token_pair_id in TokenService.blocked_token_pair_ids:
                logger.warn(LogText.BLOCKED_TOKEN)
                raise BlockedToken()
            if jwt[Strings.ROLE] not in roles:
                logger.warn(LogText.NOT_ENOUGH_PERMISSIONS.format(cls.__name__))
                raise NotEnoughPermission()

            return init(self, *args, **kwargs)

        cls.__init__ = secured_init
        return cls

    return wrapper
