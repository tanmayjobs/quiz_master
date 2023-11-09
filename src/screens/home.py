from src.helpers.constants import ScreenTexts
from src.helpers.common import invalid_choice
from src.data_containers.user import UserRole


def player_home_screen(user):
    user_choice = input(ScreenTexts.PLAYER_HOME)

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
                ...  # sign out
                return

            case other:
                invalid_choice()

    else:
        invalid_choice()


def creator_home_screen(user):
    user_choice = input(ScreenTexts.PLAYER_HOME)

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
                ...

            case 5:
                ...  # sign out
                return

            case other:
                invalid_choice()

    else:
        invalid_choice()


def admin_home_screen(user):
    user_choice = input(ScreenTexts.PLAYER_HOME)

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
                ...  # sign out
                return

            case other:
                invalid_choice()

    else:
        invalid_choice()


def home_screen(user):

    match user.role:

        case UserRole.PLAYER:
            player_home_screen()

        case UserRole.CREATOR:
            creator_home_screen()

        case UserRole.ADMIN:
            admin_home_screen()
