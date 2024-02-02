from flask_jwt_extended import JWTManager

from helpers.constants import LogText
from helpers.exceptions import TokenExpired, BlockedToken, TokenNotProvided
from helpers.log import logger


def register_jwt(app):
    logger.info(LogText.REGISTERING_JWT)
    jwt = JWTManager(app)
    jwt.expired_token_loader(lambda *_: TokenExpired().generate_response())
    jwt.invalid_token_loader(lambda *_: BlockedToken().generate_response())
    jwt.unauthorized_loader(lambda *_: TokenNotProvided().generate_response())
    logger.info(LogText.REGISTERING_JWT_COMPLETED)
