from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.quiz.add_quiz import AddQuizController
from schemas import QuizzesResponse, OkResponse, QuizResponse, QuestionsResponse, ErrorSchema, ErrorExamples, \
    QuizRequest
from services.quiz import QuizService

blp = Blueprint("Quizzes", __name__)


@blp.route("/quizzes")
class QuizzesView(MethodView):
    @blp.response(200, QuizzesResponse)
    def get(self):
        """
        Used to search, filter and get all the quizzes from the database.
        """
        ...

    @blp.arguments(QuizRequest)
    @blp.alt_response(201, schema=OkResponse)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Bearer <access_token>', 'required': 'true'}])
    def post(self, json_data):
        add_quiz = AddQuizController(json_data)
        return add_quiz()


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
