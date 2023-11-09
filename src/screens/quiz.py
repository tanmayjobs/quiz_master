from src.helpers.common import show_message


def quiz_screen(user, quiz):
    show_message(quiz.name)
    for question in quiz.questions:
        ...
