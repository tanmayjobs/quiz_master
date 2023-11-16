from constants import LogText, Errors
from helpers.common import show_message, newline
from screens.authentication.authentication import authentication_screen
from log.logger import Logger, INFO


def main():
    authentication_screen()


if __name__ == '__main__':
    Logger.log(INFO, LogText.SYSTEM_START)

    try:
        main()

    except Exception as err:
        newline()
        newline()
        show_message(Errors.UNEXPECTED_ERROR)

        Logger.log(INFO, LogText.SYSTEM_ERROR.format(err))

    finally:
        Logger.log(INFO, LogText.SYSTEM_EXIT)
