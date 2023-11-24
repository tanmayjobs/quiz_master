from helpers.constants import SQLQueries
from data_containers.question import Question
from data_containers.user import UserRole
from database import database, DBContext
from utils.rbac import accessed_by


class QuestionHandler:

    def __init__(self, quiz_id, user=None):
        self.quiz_id = quiz_id  # Quiz whose questions are being accessed
        self.user = user  # User who is trying to access the operations

    @accessed_by(UserRole.CREATOR)
    def add_question(self, question):
        with DBContext(database) as dao:
            question_id = dao.add(SQLQueries.ADD_QUESTION,
                                       (self.quiz_id, question.question_text))
            question_id = question_id.last_id

            for option in question.options:
                dao.add(SQLQueries.ADD_OPTION,
                             (question_id, option.option_text, option.is_correct))

    def get_quiz_questions(self):
        with DBContext(database) as dao:
            questions_data = dao.get(SQLQueries.GET_QUIZ_QUESTIONS,
                                          (self.quiz_id, ))
        questions = [
            Question.parse_json(question_data)
            for question_data in questions_data
        ]

        return questions

    @accessed_by(UserRole.CREATOR)
    def remove_question(self, question_id):
        with DBContext(database) as dao:
            dao.remove(SQLQueries.REMOVE_OPTION_BY_QUESTION, (question_id, ))
            dao.remove(SQLQueries.REMOVE_QUESTION, (question_id, ))
