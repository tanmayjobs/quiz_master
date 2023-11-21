from controller.quiz import QuizHandler
from controller.quiz_record import QuizRecordHandler
from helpers.constants import ScreenTexts, OutputTexts, Strings, InputTexts
from screens.quiz import QuizScreen
from utils.menu_loop import menu_loop


class PlayerScreen:

    def __init__(self, user):
        self.user = user

    def _play_random_quiz(self):
        quiz = QuizHandler.get_random_quiz()

        if not quiz:
            print()
            print(OutputTexts.NOT_YET.format(Strings.QUIZ))
            return

        QuizScreen.play_screen(self.user, quiz)

    def _explore_quiz(self):
        print()
        search_key = input(InputTexts.KEYWORD)

        all_quizzes = QuizHandler.filter_all_quizzes(search_key)
        # TODO: Implement a select quiz screen in common screens
        selected_quiz = ...

        if not selected_quiz:
            return

        QuizScreen.play_screen(self.user, selected_quiz)

    def _show_player_records_screen(self):
        print()
        player_records = QuizRecordHandler.get_user_records(self.user)

        if not player_records:
            print(OutputTexts.NO_QUIZ_RECORDS)
            return

        # TODO: Implement a show records screen in common screens
        # show_records_screen(player_records)

    @menu_loop
    def home_screen(self):
        print()
        user_choice = input(ScreenTexts.PLAYER_HOME)

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
                    return True

                case other:
                    print(OutputTexts.INVALID_CHOICE)

        else:
            print(OutputTexts.INVALID_CHOICE)

        return False
