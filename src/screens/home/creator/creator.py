from helpers.constants import ScreenTexts, OutputTexts
from utils.menu_loop import menu_loop
from screens.home_screen.common import play_random_quiz, show_player_records_screen, explore_quiz_screen
from screens.home_screen.creator.manage_quizzes.manage_quizzes import manage_quizzes_screen


@menu_loop
def creator_home_screen(creator):
    print()
    user_choice = input(ScreenTexts.CREATOR_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                play_random_quiz(creator)

            case 2:
                explore_quiz_screen(creator)

            case 3:
                show_player_records_screen(creator)

            case 4:
                manage_quizzes_screen(creator)

            case 5:
                return True

            case other:
                print(OutputTexts.INVALID_CHOICE)

    else:
        print(OutputTexts.INVALID_CHOICE)

    return False
