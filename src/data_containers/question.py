from dataclasses import dataclass
from constants import InputTexts


@dataclass
class Option:
    option_text: str
    is_correct: bool


@dataclass
class Question:
    question_id: int
    question_text: str
    options: list[Option]

    def prompt(self, question_no):
        option_1, option_2, option_3, option_4 = self.options
        return InputTexts.QUESTION_PROMPT.format(
            question_no,
            self.question_text,
            option_1.option_text,
            option_2.option_text,
            option_3.option_text,
            option_4.option_text,
        )