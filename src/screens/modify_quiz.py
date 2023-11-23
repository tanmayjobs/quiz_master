from controller.questions import QuestionHandler
from data_containers.question import Option, Question
from helpers.constants import ScreenTexts, OutputTexts, Strings, InputTexts, Numbers
from screens.common import CommonScreens
from utils.menu_loop import menu_loop


class ModifyQuizScreen:

    def __init__(self, user, quiz):
        self.user = user
        self.quiz = quiz

    @menu_loop
    def modify_quiz_screen(self):
        print()
        user_choice = input(ScreenTexts.MANAGE_QUIZ)
        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    self._list_all_questions_screen()
                case 2:
                    self._add_question_screen()
                case 3:
                    self._remove_question_screen()
                case 4:
                    return True
                case other:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)
        return False

    def _list_all_questions_screen(self):
        print()
        all_questions = QuestionHandler(self.quiz.quiz_id).get_quiz_questions()
        if not all_questions:
            print(OutputTexts.NOT_YET.format(Strings.QUESTION))
            return
        for index, question in enumerate(all_questions, start=1):
            CommonScreens.show_questions_all_info(index, question)
            print()
        print()

    def _add_question_screen(self):
        print()
        question_text = None
        while not question_text:
            question_text = input(InputTexts.QUESTION)
        options = []

        for option_no in range(Numbers.ONE, Numbers.FIVE):
            option_text = None
            while not option_text:
                option_text = input(
                    InputTexts.OPTION.format(option_no)).strip()

            option = Option(option_text, False)
            options.append(option)

        correct_option = None
        while not correct_option:
            correct_option = self._correct_option_screen()
        options[correct_option - Numbers.ONE].is_correct = True

        question = Question(Numbers.ZERO, question_text, options)
        QuestionHandler(self.quiz.quiz_id, self.user).add_question(question)
        print(OutputTexts.QUESTION_ADDED)

    @staticmethod
    def _correct_option_screen():
        print()
        correct_option = input(InputTexts.CORRECT_OPTION)
        if correct_option.isdigit():
            correct_option = int(correct_option)
            if not Numbers.ONE < correct_option > Numbers.FOUR:
                return correct_option
            else:
                print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)
        return None

    def _remove_question_screen(self):
        print()
        all_questions = QuestionHandler(self.quiz.quiz_id).get_quiz_questions()
        if not all_questions:
            print(OutputTexts.NOT_YET.format(Strings.QUESTION))
            return

        CommonScreens.show_questions(all_questions)
        selected_question = CommonScreens.select_from_list(
            all_questions, InputTexts.QUESTION_ID)
        if not selected_question:
            print(OutputTexts.INVALID_CHOICE)
            return

        QuestionHandler(self.quiz.quiz_id, self.user).remove_question(
            selected_question.question_id)
        print()
        print(OutputTexts.QUESTION_REMOVED)
