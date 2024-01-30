from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.quiz.add_quiz import AddQuizController
from controllers.quiz.get_quiz import GetQuizController
from controllers.quiz.get_quizzes import GetQuizzesController
from controllers.quiz.remove_quiz import RemoveQuizController
from helpers.constants import Strings
from helpers.constants.http_statuses import AUTHORIZATION_HEADER
from schemas import (
    QuizzesResponse,
    OkResponse,
    ErrorResponse,
    ErrorExamples,
    QuizRequest,
    QuizResponse,
)

blp = Blueprint("Quizzes", __name__)


@blp.route("/quizzes")
class QuizzesView(MethodView):
    @blp.alt_response(200, schema=QuizzesResponse)
    def get(self):
        get_quizzes = GetQuizzesController()
        return get_quizzes()

    @blp.arguments(QuizRequest)
    @blp.alt_response(201, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def post(self, json_data):
        add_quiz = AddQuizController(json_data)
        return add_quiz()


@blp.route("/quizzes/<string:quiz_id>")
class QuizView(MethodView):
    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404(Strings.QUIZ)
    )
    @blp.alt_response(200, schema=QuizResponse)
    def get(self, quiz_id):
        get_quiz = GetQuizController(quiz_id)
        return get_quiz()

    @blp.alt_response(
        404, schema=ErrorResponse, example=ErrorExamples.error404(Strings.QUIZ)
    )
    @blp.alt_response(200, schema=OkResponse)
    @blp.doc(parameters=[AUTHORIZATION_HEADER])
    def delete(self, quiz_id):
        remove_quiz = RemoveQuizController(quiz_id)
        return remove_quiz()
