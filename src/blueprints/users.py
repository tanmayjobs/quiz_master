from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.users.remove_user import RemoveUserController
from helpers.constants import Strings
from helpers.constants.http_statuses import AUTHORIZATION_HEADER
from schemas import (
    UsersResponse,
    OkResponse,
    ErrorResponse,
    UserResponse,
    ErrorExamples,
)

blp = Blueprint("Users", __name__)


@blp.route("/users")
class UsersView(MethodView):
    @blp.response(200, UsersResponse)
    def get(self):
        """
        Get all the users from the database.
        """
        ...


@blp.route("/users/<string:user_id>")
class UserView(MethodView):
    @blp.response(404, ErrorResponse, example=ErrorExamples.error404(Strings.USER))
    @blp.response(200, UserResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def get(self):
        """
        Used to get all the details about one user.
        """
        ...

    @blp.response(404, ErrorResponse, example=ErrorExamples.error404(Strings.OPTION))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def put(self):
        """
        Update information about a user.
        """
        ...

    @blp.response(404, ErrorResponse, example=ErrorExamples.error404(Strings.OPTION))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def delete(self, user_id):
        remove_user = RemoveUserController(user_id)
        return remove_user()
