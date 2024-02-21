from marshmallow.fields import String, List, Nested

from .custom_schema import CustomSchema


class UserResponse(CustomSchema):
    user_id = String(required=True)
    username = String(required=True)
    user_role = String(required=True)


class UsersResponse(CustomSchema):
    users = List(Nested(UserResponse()), required=True)
