"""
This file is the entry point of the application.
To run the program:
    cd ./src/
    python ./main.py

"""

from helpers.constants import LogText, Errors
from screens.authentication import AuthenticationScreen
from helpers.log.logger import Logger, INFO, ERROR


def main():
    AuthenticationScreen.menu_screen()


if __name__ == '__main__':
    Logger.log(INFO, LogText.SYSTEM_START)
    try:
        main()
    except Exception as err:
        print(f"\n\n{Errors.UNEXPECTED_ERROR}")
        Logger.log(ERROR, LogText.SYSTEM_ERROR.format(err))
    finally:
        Logger.log(INFO, LogText.SYSTEM_EXIT)
