import sys
import pwinput

from constants import OutputTexts, InputTexts


def invalid_choice(): print(OutputTexts.INVALID_CHOICE)


def show_message(msg): print(msg)


def pretty_print(msg): print(f'\t\t{msg}')


def password_input(): pwinput.pwinput(InputTexts.PASSWORD)


def new_line(): lambda: print()


def quit_application():
    new_line()
    print("Bye!")
    sys.exit(0)
