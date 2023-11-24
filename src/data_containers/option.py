from dataclasses import dataclass

from helpers.constants import Strings


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
