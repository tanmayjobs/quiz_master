import sys

from handler.auth import AuthHandler
from helpers.constants import ScreenTexts, OutputTexts, Errors, Messages, LogText
from helpers.log import logger
from screens.home import home_screen
from utils.inputs import get_username, get_password
from utils.menu_loop import menu_loop


class AuthenticationScreen:
    @staticmethod
    def _sign_in():
        logger.info("Sign In Screen")
        print()
        username = get_username()
        password = get_password()

        user = AuthHandler(username, password).sign_in()
        if user:
            print()
            print()
            print(Messages.GREET.format(username=user.username))
            home_screen(user)
        else:
            logger.info(LogText.INVALID_CREDENTIALS.format(username))
            print(Errors.INVALID_CREDENTIALS)

    @staticmethod
    def _sign_up():
        logger.info("Sign Up Screen")
        print()
        username = get_username()
        password = get_password()

        is_user_added = AuthHandler(username, password).sign_up()
        if is_user_added:
            print(OutputTexts.USER_ADDED)
        else:
            print(Errors.USERNAME_ALREADY_EXISTS)

    @staticmethod
    @menu_loop
    def menu_screen():
        logger.info("Authentication Screen")
        print()
        user_choice = input(ScreenTexts.AUTHENTICATION)
        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    AuthenticationScreen._sign_in()
                case 2:
                    AuthenticationScreen._sign_up()
                case 3:
                    print("\nBye!")
                    sys.exit(0)
                case other:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
