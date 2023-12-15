import json
from dataclasses import dataclass

from data_containers.option import Option
from helpers.constants import InputTexts, Strings, Numbers


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

    @staticmethod
    def parse_json(json_data):
        question_id, question_text, option_json = json_data
        options_json = json.loads(Strings.ARRAY.format(option_json))

        options = [Option.parse_json(option_json) for option_json in options_json]

        question = Question(question_id, question_text, options)
        return question
