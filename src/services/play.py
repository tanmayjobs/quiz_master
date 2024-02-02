from database import MysqlAccess, resource_database
from helpers.constants import Strings, SQLQueries


class PlayService:
    def play(self, questions, answers):
        question_ids = [question[Strings.QUESTION_ID] for question in questions]
        answer_question_ids = [answer[Strings.QUESTION_ID] for answer in answers]

        if answer_question_ids != question_ids:
            raise NotImplemented

        question_correct_options = {
            question[Strings.QUESTION_ID]: {
                option
                for option in question[Strings.OPTIONS]
                if option[Strings.IS_CORRECT]
            }
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
