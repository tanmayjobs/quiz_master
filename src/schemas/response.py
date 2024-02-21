from marshmallow.fields import Integer, String, List, Dict

from .custom_schema import CustomSchema


class ErrorResponse(CustomSchema):
    code = Integer(required=True)
    status = String(required=True)
    error = String(required=True)
    hints = List(Dict)


class OkResponse(CustomSchema):
    result = String(required=True)
