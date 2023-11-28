"""
This file is the entry point of the application.
To run the program:
    cd ./src/
    python ./main.py

"""

from helpers.constants import LogText, Errors
from helpers.log import logger
from screens.authentication import AuthenticationScreen


def main():
    AuthenticationScreen.menu_screen()


if __name__ == "__main__":
    logger.info(LogText.SYSTEM_START)
    try:
        main()
    except Exception as err:
        print(f"\n\n{Errors.UNEXPECTED_ERROR}")
        logger.info(LogText.SYSTEM_ERROR.format(err))
    finally:
        logger.info(LogText.SYSTEM_EXIT)
