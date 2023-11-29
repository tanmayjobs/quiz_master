from handler.quiz import QuizHandler
from handler.user import UserHandler
from helpers.constants import (
    ScreenTexts,
    OutputTexts,
    Messages,
    InputTexts,
    Errors,
    Strings,
)
from helpers.log import logger
from screens.common import CommonScreens
from utils.inputs import get_username, get_password
from utils.menu_loop import menu_loop


class AdminScreen:
    def __init__(self, user):
        self.user = user

    def _add_creator_screen(self):
        logger.info("Add Creator Screen")
        print()
        print(Messages.CREATOR_INFO)
        username = get_username()
        password = get_password()

        is_user_added = UserHandler(self.user).add_user(username, password)
        if is_user_added:
            print(OutputTexts.CREATOR_ADDED)
        else:
            print(Errors.USERNAME_ALREADY_EXISTS)

    def _remove_user_screen(self):
        logger.info("Remove User Screen")
        print()
        user_handler = UserHandler(self.user)
        all_users = user_handler.get_all_users()

        if not all_users:
            print(OutputTexts.NOT_YET.format(Strings.USER))
            return

        CommonScreens.show_users(all_users)
        user_for_removal = CommonScreens.select_from_list(all_users, InputTexts.USER_ID)

        if not user_for_removal:
            print(OutputTexts.INVALID_CHOICE)
            return
        user_handler.remove_user(user_for_removal.user_id)
        print(OutputTexts.USER_REMOVED)

    def _remove_quiz_screen(self):
        logger.info("Remove Quiz Screen")
        all_quizzes = QuizHandler(self.user).get_all_quizzes()
        CommonScreens.show_quizzes(all_quizzes)
        quiz_to_remove = CommonScreens.select_from_list(all_quizzes, InputTexts.QUIZ_ID)

        if not quiz_to_remove:
            print(OutputTexts.INVALID_CHOICE)
            return
        QuizHandler(self.user, quiz_to_remove).remove_quiz()
        print()
        print(OutputTexts.QUIZ_REMOVED)

    @menu_loop
    def home_screen(self):
        logger.info("Admin Home Screen")
        print()
        user_choice = input(ScreenTexts.ADMIN_HOME)

        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    self._add_creator_screen()
                case 2:
                    self._remove_user_screen()
                case 3:
                    self._remove_quiz_screen()
                case 4:
                    return True
                case _:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
