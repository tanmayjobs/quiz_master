from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.auth.logout import LogoutController
from controllers.auth.refresh import RefreshTokenController
from controllers.auth.sign_in import SignInController
from controllers.auth.sign_up import SignUpController
from helpers.constants import Strings
from schemas import (
    AuthRequest,
    TokensResponse,
    ErrorResponse,
    OkResponse,
    ErrorExamples,
)

blp = Blueprint("Auth", __name__, url_prefix="/auth")


@blp.route("/sign_in")
class SignIn(MethodView):
    @blp.arguments(AuthRequest)
    @blp.alt_response(401, schema=ErrorResponse, example=ErrorExamples.error401())
    @blp.alt_response(200, schema=TokensResponse)
    def post(self, json_data):
        sign_in = SignInController(json_data)
        return sign_in()


@blp.route("/sign_up")
class SignUp(MethodView):
    @blp.arguments(AuthRequest)
    @blp.alt_response(201, schema=OkResponse)
    @blp.alt_response(
        409, schema=ErrorResponse, example=ErrorExamples.error409(Strings.USERNAME)
    )
    def post(self, json_data):
        sign_up = SignUpController(json_data)
        return sign_up()


@blp.route("/refresh")
class Refresh(MethodView):
    @blp.alt_response(200, schema=TokensResponse)
    def post(self):
        refresh_token = RefreshTokenController()
        return refresh_token()


@blp.route("/logout")
class Logout(MethodView):
    def post(self):
        logout = LogoutController()
        return logout()
