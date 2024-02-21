from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.quiz import QuizService


class GetQuizController:
    def __init__(self, quiz_id, quiz_service=None):
        self.quiz_id = quiz_id
        self.quiz_service = quiz_service or QuizService()

    def __call__(self):
        try:
            quiz = self.quiz_service.get_quiz(self.quiz_id)
        except CustomException as custom_error:
            request_logger.warn(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return quiz, HTTPStatuses.OK.code