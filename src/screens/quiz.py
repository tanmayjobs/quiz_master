from handler.questions import QuestionHandler
from handler.quiz_record import QuizRecordHandler
from data_containers.question import Option
from data_containers.quiz_record import QuizRecord
from helpers.constants import Messages, OutputTexts, Strings, Numbers


class QuizScreen:

    @staticmethod
    def play_quiz(all_questions):
        player_score = 0
        for question_no, question in enumerate(all_questions, start=1):
            print()
            answer = None
            correct_option = [
                option for option in question.options if option.is_correct
            ][0]

            while not isinstance(answer, Option):
                answer = input(question.prompt(question_no))
                if answer.isdigit():
                    answer = int(answer)
                    if Numbers.ONE <= answer <= Numbers.FOUR:
                        answer = question.options[answer - Numbers.ONE]
                    else:
                        print(OutputTexts.INVALID_CHOICE)
                else:
                    print(OutputTexts.INVALID_CHOICE)
                print()

            if answer.is_correct:
                player_score += 1
                print(
                    Messages.CORRECT_GUESS.format(
                        option_text=answer.option_text))
            else:
                print(
                    Messages.INCORRECT_GUESS.format(
                        option_text=correct_option.option_text))
            print()
        return player_score

    @staticmethod
    def play_screen(user, quiz):
        print()
        print()
        print(
            Messages.QUIZ_NAME.format(quiz_name=quiz.quiz_name,
                                      creator_name=quiz.creator_name))

        all_questions = QuestionHandler(quiz.quiz_id,
                                        user).get_quiz_questions()
        if not all_questions:
            print(Messages.WORKING_ON_QUIZ)
            return

        total_score = len(all_questions)
        player_score = QuizScreen.play_quiz(all_questions)
        quiz_record = QuizRecord(user.user_id, user.username, quiz.quiz_id,
                                 quiz.quiz_name, player_score, total_score)
        QuizRecordHandler.add_quiz_record(quiz_record)
        QuizScreen.show_quiz_result(quiz_record)

    @staticmethod
    def show_quiz_result(quiz_record: QuizRecord):
        print()
        print(
            OutputTexts.QUIZ_RESULT.format(
                result=(quiz_record.player_score / quiz_record.total_score) *
                100,
                quiz_name=quiz_record.quiz_name))
        print()

        top_records = QuizRecordHandler.quiz_top_records(quiz_record.quiz_id)
        if top_records:
            print(Messages.TOP_RECORD)
            print(
                OutputTexts.RECORD_INFO.format(record_id=Strings.ID,
                                               quiz_name=Strings.QUIZ,
                                               player_name=Strings.PLAYER,
                                               result=Strings.RESULT,
                                               played_at=Strings.PLAYED_AT))

            for index, record in enumerate(top_records, start=1):
                result = (record.player_score / record.total_score) * 100
                print(
                    OutputTexts.RECORD_INFO.format(
                        record_id=str(index),
                        quiz_name=record.quiz_name,
                        player_name=record.player_name,
                        result=Strings.RESULT_PERCENTAGE.format(result),
                        played_at=record.played_at))
            print()
