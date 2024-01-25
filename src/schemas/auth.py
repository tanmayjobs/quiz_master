from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema
from marshmallow.fields import String, validate


class AuthRequest(CustomSchema):
    username = String(required=True, validate=validate.Regexp(RegexPatterns.USERNAME))
    password = String(required=True, load_only=True)


class SignInResponse(CustomSchema):
    access_token = String(dump_only=True)
