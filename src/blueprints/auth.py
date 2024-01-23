from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.auth.sign_in import SignInController
from controllers.auth.sign_up import SignUpController
from schemas import AuthRequest, SignInResponse, ErrorResponse, OkResponse, ErrorExamples

blp = Blueprint("Auth", __name__, url_prefix="/auth")


@blp.route("/sign_in")
class SignIn(MethodView):
    @blp.arguments(AuthRequest)
    @blp.alt_response(401, schema=ErrorResponse, example=ErrorExamples.error401())
    @blp.alt_response(200, schema=SignInResponse)
    def post(self, json_data):
        sign_in = SignInController(json_data)
        return sign_in()


@blp.route("/sign_up")
class SignUp(MethodView):
    @blp.arguments(AuthRequest)
    @blp.alt_response(201, schema=OkResponse)
    @blp.alt_response(409, schema=ErrorResponse, example=ErrorExamples.error409("username"))
    def post(self, json_data):
        sign_up = SignUpController(json_data)
        return sign_up()
