import pwinput

from controller.quiz import QuizHandler
from controller.user import UserHandler
from helpers.constants import ScreenTexts, OutputTexts, Messages, InputTexts, Errors, Strings
from screens.common import CommonScreens
from utils.crypt import validate_password
from utils.menu_loop import menu_loop
from utils.validators import Validators


class AdminScreen:

    def __init__(self, user):
        self.user = user

    def add_creator_screen(self):
        print()
        print(Messages.CREATOR_INFO)
        username, password = Validators.get_username(), Validators.get_password()

        is_user_added = UserHandler(self.user).add_user(username, password)
        if is_user_added:
            print(OutputTexts.CREATOR_ADDED)
        else:
            print(Errors.USERNAME_ALREADY_EXISTS)

    def remove_user_screen(self):
        print()
        user_handler = UserHandler(self.user)
        all_users = user_handler.get_all_users()

        if not all_users:
            print(OutputTexts.NOT_YET.format(Strings.USER))
            return

        CommonScreens.show_users(all_users)
        user_for_removal = CommonScreens.select_from_list(
            all_users, InputTexts.USER_ID)

        if not user_for_removal:
            print(OutputTexts.INVALID_CHOICE)
            return
        user_handler.remove_user(user_for_removal.user_id)
        print(OutputTexts.USER_REMOVED)

    def remove_quiz_screen(self):
        all_quizzes = QuizHandler(self.user).get_all_quizzes()
        CommonScreens.show_quizzes(all_quizzes)
        quiz_to_remove = CommonScreens.select_from_list(
            all_quizzes, InputTexts.QUIZ_ID)

        if not quiz_to_remove:
            print(OutputTexts.INVALID_CHOICE)
            return
        QuizHandler(self.user, quiz_to_remove).remove_quiz()
        print()
        print(OutputTexts.QUIZ_REMOVED)

    @menu_loop
    def home_screen(self):
        print()
        user_choice = input(ScreenTexts.ADMIN_HOME)

        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    self.add_creator_screen()
                case 2:
                    self.remove_user_screen()
                case 3:
                    self.remove_quiz_screen()
                case 4:
                    return True
                case other:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
