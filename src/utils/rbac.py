from flask_jwt_extended import verify_jwt_in_request, get_jwt

from helpers.log import logger
from services.tokens import TokenService
from helpers.constants import Strings, LogText
from helpers.exceptions import NotEnoughPermission, BlockedToken


def validate_token_details(*roles: str, check_fresh=False, refresh=False):
    """
    This function is used as a decorator on classes and extend their functionality by applying RBAC.
    :param roles: Takes multiple roles which can access the class. Use UserRole.[ROLE].value.
    :param check_fresh: Default False, will check weather or not the token is fresh in case of True. Can be used for more secured endpoints.
    :param refresh: Default False, will check the type of token is refresh or not in case of True.
    :return: Return the modifies class. You know how decorators work, right?
    """

    def wrapper(cls):
        init = cls.__init__  # Creating reference to original __init__

        def secured_init(self, *args, **kwargs):
            """
            This functions validates the token as per the refresh and check_fresh values.
            Then check weather the token is blocked or not.
            And then checks the valid role.

            Can raise BlockedToken or NotEnoughPermission which are being handled on the top flask level.
            :param self: You know this.
            :param args: You know this too.
            :param kwargs: You know everything.
            :return: Returns what original __init__ returns, None.
            """
            verify_jwt_in_request(fresh=check_fresh, refresh=refresh, verify_type=True)  # Verifying the token
            jwt = get_jwt()
            token_pair_id = jwt[Strings.TOKEN_PAIR_ID]

            if TokenService().is_blocked(token_pair_id):    # Verifying weather the token is blocked or not
                logger.warn(LogText.BLOCKED_TOKEN)
                raise BlockedToken()

            if jwt[Strings.ROLE] not in roles:  # Verifying correct role
                logger.warn(LogText.NOT_ENOUGH_PERMISSIONS.format(cls.__name__))
                raise NotEnoughPermission()

            return init(self, *args, **kwargs)

        cls.__init__ = secured_init  # Overriding the __init__ method of the class with secured_init
        return cls

    return wrapper
