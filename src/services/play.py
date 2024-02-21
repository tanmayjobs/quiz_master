from helpers.constants import Strings, Errors
from helpers.exceptions import DoNotExists, InvalidQuizResponse


class PlayService:
    def play(self, questions, answers):
        question_ids = {question[Strings.QUESTION_ID] for question in questions}
        answer_question_ids = {answer[Strings.QUESTION_ID] for answer in answers}

        if answer_question_ids != question_ids:
            raise InvalidQuizResponse(
                Errors.INVALID_QUIZ_QUESTION, {
                    Strings.MISSING_QUESTIONS: list(question_ids - answer_question_ids),
                    Strings.EXTRA_QUESTIONS: list(answer_question_ids - question_ids),
                }
            )

        question_correct_options = {
            question[Strings.QUESTION_ID]: [
                option[Strings.ID]
                for option in question[Strings.OPTIONS]
                if option[Strings.IS_CORRECT]
            ]
            for question in questions
        }
        questions = {
            question[Strings.QUESTION_ID]: question
            for question in questions
        }

        total_score = 0.0
        for answer in answers:
            selected_options = set(answer[Strings.SELECT_OPTION_IDS])
            correct_options = set(question_correct_options[answer[Strings.QUESTION_ID]])
            correct_selected = correct_options - selected_options
            incorrect_selected = selected_options - correct_selected
            each_question_score = (
                len(correct_selected) - len(incorrect_selected)
            ) / len(questions[answer[Strings.QUESTION_ID]][Strings.OPTIONS])
            total_score += each_question_score

        return total_score
