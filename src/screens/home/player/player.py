from constants import ScreenTexts
from screens.common import invalid_choice, newline
from utils.menu_loop import menu_loop
from screens.home.common import play_random_quiz, show_player_records_screen, explore_quiz_screen


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
                explore_quiz_screen(player)

            case 3:
                show_player_records_screen(player)

            case 4:
                return True

            case other:
                invalid_choice()

    else:
        invalid_choice()

    return False
