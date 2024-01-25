from helpers.constants import RegexPatterns
from .custom_schema import CustomSchema
from marshmallow.fields import Integer, String, List, Dict, validate


class ErrorResponse(CustomSchema):
    code = Integer(required=True)
    status = String(required=True)
    error = String(required=True)
    hints = List(Dict)


class OkResponse(CustomSchema):
    result = String(required=True)
