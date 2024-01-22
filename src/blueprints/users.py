from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import UsersResponse, OkResponse, ErrorResponse, UserDetail, UserResponse, ErrorSchema, ErrorExamples

blp = Blueprint("Users", __name__)


@blp.route("/users")
class UsersView(MethodView):
    @blp.response(200, UsersResponse)
    def get(self):
        """
        Get all the users from the database.
        """
        ...


@blp.route("/users/<int:user_id>")
class UserView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("user"))
    @blp.response(200, UserResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def get(self):
        """
        Used to get all the details about one user.
        """
        ...

    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("options"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def put(self):
        """
        Update information about a user.
        """
        ...

    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("options"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self):
        """
        Delete a user.
        """
        ...
