import pwinput

from controller.quiz import QuizHandler
from controller.user import UserHandler
from helpers.constants import ScreenTexts, OutputTexts, Messages, InputTexts, Errors, Strings
from utils.crypt import validate_password
from utils.menu_loop import menu_loop


class AdminScreen:
    def __init__(self, user):
        self.user = user

    def add_creator_screen(self):
        print()
        print(Messages.CREATOR_INFO)
        username, password = input(InputTexts.USERNAME), pwinput.pwinput(InputTexts.PASSWORD)

        if not username:
            print(Errors.USERNAME_EMPTY)
            return
        if not validate_password(password):
            print(Errors.WEAK_PASSWORD)
            return

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

        # TODO: Implement the next two methods
        # show_all_users(all_users)
        # user_for_removal = select_user(all_users)
        user_for_removal = ...
        if not user_for_removal:
            print(OutputTexts.INVALID_CHOICE)
            return
        user_handler.remove_user(user_for_removal.user_id)
        print(OutputTexts.USER_REMOVED)

    def remove_quiz_screen(self):
        all_quizzes = QuizHandler(self.user).get_all_quizzes()
        # TODO: Implement the next method in common screen
        # quiz_to_remove = select_quiz_screen(all_quizzes)
        quiz_to_remove = ...
        if not quiz_to_remove:
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
