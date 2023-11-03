class Question:
    def __init__(self, question: str, marks: int, options: list[str], correct_options: list[str]):
        self.question = question
        self.marks = marks
        self.options = options
        self.correct_options = correct_options


class Quiz:
    def __init__(self, quiz_id: int, creator_id: int, name: str, types: str, questions: list[Question]):
        self.quiz_id = quiz_id
        self.creator_id = creator_id
        self.name = name
        self.types = types
        self.questions = questions
        self.total_score = sum((question.marks for question in questions))

    @staticmethod
    def get():
        ...

    @staticmethod
    def add(self):
        ...

    def remove(self):
        ...
