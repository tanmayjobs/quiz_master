import typing

from marshmallow import Schema, ValidationError
from marshmallow.fields import Integer, String, List, Enum, Boolean, Nested, validate

from helpers.enum.user_role import UserRole


class ValidationCustomException(Exception):
    def __init__(self, error):
        self.error = error


class CustomSchema(Schema):
    def handle_error(
            self, error: ValidationError, data: typing.Any, *, many: bool, **kwargs
    ):
        raise ValidationCustomException(error)


class AuthRequest(CustomSchema):
    username = String(required=True, validate=validate.Regexp("^[a-zA-Z]+[a-zA-Z0-9]*$"))
    password = String(required=True, load_only=True)


class SignInResponse(Schema):
    access_token = String(dump_only=True)


class ErrorResponse(Schema):
    code = Integer(required=True, dump_only=True)
    error = String(required=True, dump_only=True)
    message = String(required=True, dump_only=True)


class OkResponse(Schema):
    result = String(dump_default="ok")


class TagId(Schema):
    tag_id = String(required=True, dump_only=True)


class TagName(Schema):
    tag_name = String(required=True)


class Tag(TagId, TagName):
    ...


class TagsResponse(Schema):
    tags = List(Nested(Tag()), required=True)


class Option(Schema):
    option = String(required=True)
    is_correct = Boolean(required=True, load_only=True)


class Question(Schema):
    question = String(required=True)
    options = List(Nested(Option()), required=True, validate=validate.Length(min=1))


class QuizSchema(Schema):
    quiz_id = String(required=True, dump_only=True)
    quiz_name = String(required=True, dump_only=True)
    creator_id = String(required=True, dump_only=True)
    creator_name = String(required=True, dump_only=True)
    tags = List(Nested(Tag()), required=True, dump_only=True)
    questions = List(Nested(Question()), required=True, validate=validate.Length(min=1))


class TagResponse(Schema):
    tag = Nested(Tag(), required=True)


class QuizzesResponse(Schema):
    quizzes = List(Nested(QuizSchema()), required=True, dump_only=True)


class QuestionsResponse(Schema):
    questions = List(Nested(Question()), required=True)


class UserDetail(Schema):
    id = String(required=True, dump_only=True)
    username = String(required=True, dump_only=True)
    role = Enum(UserRole, required=True, dump_only=True)


class UserResponse(Schema):
    user = Nested(UserDetail(), required=True, dump_only=True)


class UsersResponse(Schema):
    users = List(Nested(UserDetail()), required=True, dump_only=True)


class ErrorSchema(Schema):
    code = Integer()
    error = String()
    message = String()
    hint = String()


class ErrorExamples:
    @staticmethod
    def error404(resource):
        return {"code": 404, "error": "Not Found", "message": f"{resource} not found!"}

    @staticmethod
    def error409(resource):
        return {"code": 409, "error": "Conflict", "message": f"conflict arise for {resource}"}

    @staticmethod
    def error401():
        return {"code": 401, "error": "Unauthorize", "message": "invalid credentials"}


class QuizRequest(Schema):
    quiz_name = String(required=True, load_only=True)
    tags = List(String, required=True, validate=validate.Length(min=1))
    questions = List(Nested(Question()), required=True, validate=validate.Length(min=1))
