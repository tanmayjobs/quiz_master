from helpers.constants import ScreenTexts, OutputTexts
from helpers.log import logger
from screens.manage_quizzes import ManageQuizScreen
from screens.player import PlayerScreen
from utils.menu_loop import menu_loop


class CreatorScreen(PlayerScreen):
    def _manage_quiz_screen(self):
        return ManageQuizScreen(self.user).manage_quizzes_screen()

    @menu_loop
    def home_screen(self):
        logger.info("Creator Home Screen")
        print()
        user_choice = input(ScreenTexts.CREATOR_HOME)

        if user_choice.isdigit():
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    self._play_random_quiz()
                case 2:
                    self._explore_quiz()
                case 3:
                    self._show_player_records_screen()
                case 4:
                    self._manage_quiz_screen()
                case 5:
                    return True
                case _:
                    print(OutputTexts.INVALID_CHOICE)

        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
