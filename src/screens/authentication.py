import sys
from logging import WARN
import pwinput

from controller.auth import AuthHandler
from helpers.constants import ScreenTexts, OutputTexts, InputTexts, Errors, Messages, LogText
from helpers.log.logger import Logger
from screens.home import home_screen
from utils.crypt import validate_password
from utils.menu_loop import menu_loop
from utils.validators import Validators


class AuthenticationScreen:

    @staticmethod
    def sign_in():
        print()
        username, password = Validators.get_username(), Validators.get_password()

        user = AuthHandler(username, password).sign_in()
        if user:
            print()
            print()
            print(Messages.GREET.format(username=user.username))
            home_screen(user)
        else:
            Logger.log(WARN, LogText.INVALID_CREDENTIALS.format(username))
            print(Errors.INVALID_CREDENTIALS)

    @staticmethod
    def sign_up():
        print()
        username, password = Validators.get_username(), Validators.get_password()

        is_user_added = AuthHandler(username, password).sign_up()
        if is_user_added:
            print(OutputTexts.USER_ADDED)
        else:
            print(Errors.USERNAME_ALREADY_EXISTS)

    @staticmethod
    @menu_loop
    def menu_screen():
        print()
        user_choice = input(ScreenTexts.AUTHENTICATION)

        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    AuthenticationScreen.sign_in()
                case 2:
                    AuthenticationScreen.sign_up()
                case 3:
                    print("\nBye!")
                    sys.exit(0)
                case other:
                    print(OutputTexts.INVALID_CHOICE)
        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
