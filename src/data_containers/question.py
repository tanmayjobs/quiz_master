import json
from dataclasses import dataclass
from constants import InputTexts, Strings, Numbers


@dataclass
class Option:
    option_text: str
    is_correct: bool

    @staticmethod
    def parse_json(json_data):
        option = Option(
            option_text=json_data[Strings.OPTION.lower()],
            is_correct=json_data[Strings.IS_CORRECT],
        )
        return option


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
        question_id = json_data[Numbers.ZERO]
        question_text = json_data[Strings.QUESTION_TEXT]
        options_json = json.loads(
            Strings.ARRAY.format(
                json_data[Strings.OPTIONS_JSON]
            )
        )

        options = [Option.parse_json(option_json) for option_json in options_json]

        question = Question(
            question_id,
            question_text,
            options
        )
        return question
