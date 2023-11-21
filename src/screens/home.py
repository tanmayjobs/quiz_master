from helpers.constants import OutputTexts
from screens.creator import creator_home_screen
from screens.home.admin.admin import admin_home_screen
from data_containers.user import UserRole
from screens.player import PlayerScreen


def home_screen(user):

    match user.role:

        case UserRole.PLAYER:
            PlayerScreen(user).player_home_screen()

        case UserRole.CREATOR:
            creator_home_screen(user)

        case UserRole.ADMIN:
            admin_home_screen(user)

    print()
    print(OutputTexts.SIGN_OUT)
