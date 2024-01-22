from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import AuthRequest, SignInResponse, ErrorResponse, OkResponse, ErrorExamples

blp = Blueprint("Auth", __name__)


@blp.route("/sign_in")
class SignIn(MethodView):
    @blp.arguments(AuthRequest)
    @blp.response(200, SignInResponse)
    @blp.response(401, ErrorResponse, example=ErrorExamples.error401())
    def post(self):
        """
        Used for authentication and to get access token.
        """
        ...


@blp.route("/sign_up")
class SignUp(MethodView):
    @blp.arguments(AuthRequest)
    @blp.response(201, OkResponse)
    @blp.response(409, ErrorResponse, example=ErrorExamples.error409("username"))
    def post(self):
        """
        Used to register a new account can be a player or a creator.
        """
        ...
