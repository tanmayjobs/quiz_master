from flask_jwt_extended import JWTManager

from helpers.exceptions import TokenExpired, BlockedToken, TokenNotProvided


def register_jwt(app):
    jwt = JWTManager(app)
    jwt.expired_token_loader(lambda *_: TokenExpired().generate_response())
    jwt.invalid_token_loader(lambda *_: BlockedToken().generate_response())
    jwt.unauthorized_loader(lambda *_: TokenNotProvided().generate_response())
