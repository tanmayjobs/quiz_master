from constants import ScreenTexts
from helpers.common import invalid_choice, newline
from helpers.menu_loop import menu_loop
from screens.home.common import play_quiz_screen, play_random_quiz, show_records_screen


@menu_loop
def player_home_screen(player):
    newline()
    user_choice = input(ScreenTexts.PLAYER_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                play_random_quiz(player)

            case 2:
                ...

            case 3:
                show_records_screen(player)

            case 4:
                ...  # sign out
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
