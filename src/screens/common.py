from helpers.constants import OutputTexts, InputTexts, Strings
from data_containers.question import Question
from data_containers.quiz_record import QuizRecord
from data_containers.user import UserRole


class CommonScreens:

    @staticmethod
    def select_multiple_from_list(items):
        indexes = input(InputTexts.TYPE_IDS).split(",")
        if not indexes:
            return None

        selected_items = []
        for index in indexes:
            if not index.isdigit():
                return None
            index = int(index) - 1
            if index < 0 or index > len(items) - 1:
                return None
            selected_items.append(items[index])

        return selected_items

    @staticmethod
    def select_from_list(items, input_message):
        index = input(input_message)
        if not index.isdigit():
            return None

        index = int(index) - 1
        if index < 0 or index > len(items) - 1:
            return None

        return items[index]

    @staticmethod
    def show_quizzes(quizzes):
        print(
            OutputTexts.QUIZ_INFO.format(
                quiz_id=Strings.ID,
                quiz_name=Strings.QUIZ,
                quiz_types=Strings.TYPE,
            )
        )

        for index, quiz in enumerate(quizzes, start=1):
            print(
                OutputTexts.QUIZ_INFO.format(
                    quiz_id=str(index),
                    quiz_name=quiz.quiz_name,
                    quiz_types=','.join(quiz_type.type_name for quiz_type in quiz.types),
                )
            )

    @staticmethod
    def show_all_types(all_types):
        print(OutputTexts.TYPE_INFO.format(type_id=Strings.ID,type_name=Strings.TYPE))

        for index, each_type in enumerate(all_types, start=1):
            print(OutputTexts.TYPE_INFO.format(type_id=str(index),type_name=each_type.type_name))

    @staticmethod
    def show_questions(questions):
        info_message = OutputTexts.QUESTION_INFO

        print(info_message.format(question_id=Strings.ID, question_text=Strings.QUESTION))
        for index, question in enumerate(questions, start=1):
            print(OutputTexts.QUESTION_INFO.format(question_id=str(index), question_text=question.question_text))

    @staticmethod
    def show_users(users):
        print(
            OutputTexts.USER_INFO.format(
                user_id=Strings.ID,
                username=Strings.USERNAME,
                user_role=Strings.ROLE
            )
        )

        for index, user in enumerate(users, start=1):
            print(
                OutputTexts.USER_INFO.format(
                    user_id=str(index),
                    username=user.username,
                    user_role=UserRole.to_string(user.role)
                )
            )

    @staticmethod
    def show_questions_all_info(index, question: Question):
        correct_option = [option for option in question.options if option.is_correct]
        correct_option = correct_option[0]

        print(
            OutputTexts.QUESTION_ALL_INFO.format(
                question_id=str(index),
                question_text=question.question_text,
                option_1=question.options[0].option_text,
                option_2=question.options[1].option_text,
                option_3=question.options[2].option_text,
                option_4=question.options[3].option_text,
                correct_option=correct_option.option_text
            )
        )

    @staticmethod
    def show_record(index, record: QuizRecord):
        result = (record.player_score / record.total_score) * 100
        print(
            OutputTexts.RECORD_INFO.format(
                record_id=str(index),
                quiz_name=record.quiz_name,
                player_name=record.player_name,
                result=Strings.RESULT_PERCENTAGE.format(result),
                played_at=record.played_at
            )
        )

