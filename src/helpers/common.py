import sys
import pwinput

from constants import OutputTexts, InputTexts

invalid_choice = lambda: print(OutputTexts.INVALID_CHOICE)
show_message = lambda x: print(x)
pretty_print = lambda msg: print(f'\t\t{msg}')
password_input = lambda : pwinput.pwinput(InputTexts.PASSWORD)
new_line = lambda : print()


def quit():
    new_line()
    print("Bye!")
    sys.exit(0)
