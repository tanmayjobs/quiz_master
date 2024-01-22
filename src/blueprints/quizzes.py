from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import QuizzesResponse, OkResponse, QuizResponse, QuestionsResponse, ErrorSchema, ErrorExamples

blp = Blueprint("Quizzes", __name__)


@blp.route("/quizzes")
class QuizzesView(MethodView):
    @blp.response(200, QuizzesResponse)
    def get(self):
        """
        Used to search, filter and get all the quizzes from the database.
        """
        ...

    @blp.response(201, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self):
        """
        Used to create a new quiz.
        """
        ...


@blp.route("/quizzes/<int:quiz_id>")
class QuizView(MethodView):
    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("quiz"))
    @blp.response(200, QuizResponse)
    def get(self, quiz_id):
        """
        Used to get all the details(questions, leaderboard, etc.) about one quiz. Allows partial response.
        """
        ...

    @blp.response(404, ErrorSchema, example=ErrorExamples.error404("quiz"))
    @blp.response(200, OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def delete(self, quiz_id):
        """
        Used to delete a quiz.
        """
        ...
