from src.helpers.constants import MenuTexts
from src.helpers.common import invalid_choice


def player_home_menu(user):
    user_choice = input(MenuTexts.PLAYER_HOME)

    if user_choice.isdigit():

        user_choice = int(user_choice)
        match user_choice:

            case 1:
                ...

            case 2:
                ...

            case 3:
                ...

            case 4:
                return

            case other:
                invalid_choice()

    else:
        invalid_choice()
