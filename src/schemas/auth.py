from marshmallow.fields import String, validate

from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema


class AuthRequest(CustomSchema):
    username = String(required=True, validate=validate.Regexp(RegexPatterns.USERNAME))
    password = String(required=True, load_only=True)


class TokensResponse(CustomSchema):
    access_token = String(dump_only=True)
    refresh_token = String(dump_only=True)
