from screens.home.player.player import player_home_screen
from screens.home.creator.creator import creator_home_screen
from screens.home.admin.admin import admin_home_screen
from data_containers.user import UserRole


def home_screen(user):

    match user.role:

        case UserRole.PLAYER:
            player_home_screen(user)

        case UserRole.CREATOR:
            creator_home_screen(user)

        case UserRole.ADMIN:
            admin_home_screen(user)
