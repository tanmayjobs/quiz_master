from helpers.constants import Strings, Errors
from helpers.exceptions import DoNotExists, InvalidQuizResponse
from helpers.log import request_logger


class PlayService:
    def play(self, questions, answers):
        question_ids = [question[Strings.QUESTION_ID] for question in questions]
        answer_question_ids = [answer[Strings.QUESTION_ID] for answer in answers]

        if answer_question_ids != question_ids:
            raise InvalidQuizResponse(Errors.INVALID_QUIZ_ANSWERS)

        question_correct_options = {
            question[Strings.QUESTION_ID]: [
                option[Strings.ID]
                for option in question[Strings.OPTIONS]
                if option[Strings.IS_CORRECT]
            ]
            for question in questions
        }

        total_score = 0.0
        for answer in answers:
            selected_options = set(answer[Strings.SELECT_OPTION_IDS])
            correct_options = set(question_correct_options[answer[Strings.QUESTION_ID]])
            correct_selected = correct_options.intersection(selected_options)
            incorrect_selected = selected_options - correct_selected
            each_question_score = (
                len(correct_selected) - len(incorrect_selected)
            ) / len(question_correct_options[answer[Strings.QUESTION_ID]])
            total_score += each_question_score
        return total_score
