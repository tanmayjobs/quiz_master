from marshmallow import Schema
from marshmallow.fields import Integer, String, List, Enum, Boolean, Nested

from helpers.enum.user_role import UserRole


class AuthRequest(Schema):
    username = String(required=True)
    password = String(required=True, load_only=True)


class SignInResponse(Schema):
    result = String(dump_only=True)
    access_token = String(dump_only=True)


class ErrorResponse(Schema):
    code = Integer(required=True, dump_only=True)
    status = String(required=True, dump_only=True)
    message = String(required=True, dump_only=True)


class OkResponse(Schema):
    result = String(dump_default="ok")


class Tag(Schema):
    id = Integer(required=True, dump_only=True)
    name = String(required=True, dump_only=True)


class Quiz(Schema):
    id = Integer(required=True, dump_only=True)
    name = String(required=True, dump_only=True)
    creator_id = Integer(required=True, dump_only=True)
    tags = List(Nested(Tag()), required=True, dump_only=True)


class Option(Schema):
    text = String(required=True)
    is_correct = Boolean(required=True)


class Question(Schema):
    id = Integer(required=True, dump_only=True)
    text = String(required=True, dump_only=True)
    answers = List(Nested(Option()), required=True, dump_only=True)


class TagResponse(Schema):
    tag = Nested(Tag(), required=True)


class QuizResponse(Schema):
    quiz = Nested(Quiz(), required=True, dump_only=True)
    questions = List(Nested(Question()))


class QuizzesResponse(Schema):
    quizzes = List(Nested(Quiz()), required=True, dump_only=True)


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
    status = String()
    message = String()
    hint = String()


class ErrorExamples:
    @staticmethod
    def error404(resource):
        return {"code": 404, "status": "Not Found", "message": f"{resource} not found!"}

    @staticmethod
    def error409(resource):
        return {"code": 409, "status": "Conflict", "message": f"conflict arise for {resource}", "hint": f"maybe {resource} is not following unique constrains."}

    @staticmethod
    def error401():
        return {"code": 401, "status": "Unauthorize", "message": "invalid credentials"}
