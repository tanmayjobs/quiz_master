from helpers.constants import ScreenTexts, OutputTexts
from screens.manage_quizzes import ManageQuizScreen
from screens.player import PlayerScreen
from utils.menu_loop import menu_loop


class CreatorScreen(PlayerScreen):

    @menu_loop
    def home_screen(self):
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
                    ManageQuizScreen(self.user).manage_quizzes_screen()

                case 5:
                    return True

                case other:
                    print(OutputTexts.INVALID_CHOICE)

        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
