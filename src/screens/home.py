from data_containers.user import UserRole
from helpers.constants import OutputTexts
from screens.admin import AdminScreen
from screens.creator import CreatorScreen
from screens.player import PlayerScreen


def home_screen(user):
    match user.role:
        case UserRole.PLAYER.name:
            PlayerScreen(user).home_screen()
        case UserRole.CREATOR.name:
            CreatorScreen(user).home_screen()
        case UserRole.ADMIN.name:
            AdminScreen(user).home_screen()

    print()
    print(OutputTexts.SIGN_OUT)
