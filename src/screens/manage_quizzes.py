from controller.quiz import QuizHandler
from data_containers.quiz import Quiz
from helpers.constants import ScreenTexts, OutputTexts, Strings, InputTexts
from screens.common import CommonScreens
from screens.modify_quiz import ModifyQuizScreen
from utils.menu_loop import menu_loop
from utils.validators import Validators


class ManageQuizScreen:

    def __init__(self, user):
        self.user = user

    @menu_loop
    def manage_quizzes_screen(self):
        print()
        user_choice = input(ScreenTexts.MANAGE_QUIZZES)

        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    self._add_quiz_screen()
                case 2:
                    self.remove_quiz_screen()
                case 3:
                    selected_quiz = self._select_quiz_screen()
                    if selected_quiz:
                        ModifyQuizScreen(self.user,
                                         selected_quiz).modify_quiz_screen()
                case 4:
                    return True
                case other:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)

        return False

    def _select_quiz_screen(self):
        print()
        all_quizzes = QuizHandler(self.user).get_user_quizzes()
        if not all_quizzes:
            print(OutputTexts.NOT_YET.format(Strings.QUIZ))
            return

        CommonScreens.show_quizzes(all_quizzes)
        selected_quiz = CommonScreens.select_from_list(all_quizzes,
                                                       InputTexts.QUIZ_ID)

        if not selected_quiz:
            print(OutputTexts.INVALID_CHOICE)
            return
        return selected_quiz

    @staticmethod
    def _select_quiz_type():
        all_types = QuizHandler.defined_quiz_types()
        CommonScreens.show_all_types(all_types)
        selected_types = CommonScreens.select_multiple_from_list(all_types)
        if not selected_types:
            print(OutputTexts.INVALID_CHOICE)
            print()
            return None
        return selected_types

    def remove_quiz_screen(self):
        quiz_to_remove = self._select_quiz_screen()
        if not quiz_to_remove:
            return

        QuizHandler(self.user, quiz_to_remove).remove_quiz()
        print()
        print(OutputTexts.QUIZ_REMOVED)

    def _add_quiz_screen(self):
        print()
        quiz_name = Validators.get_valid_strings(InputTexts.QUIZ_NAME)
        quiz_types = None

        while not quiz_types:
            quiz_types = self._select_quiz_type()

        quiz = Quiz(quiz_id=None,
                    quiz_name=quiz_name,
                    creator_id=self.user.user_id,
                    creator_name=self.user.username,
                    types=quiz_types)

        QuizHandler(self.user, quiz).add_quiz()

        print()
        print(OutputTexts.QUIZ_ADDED)
