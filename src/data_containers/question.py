from dataclasses import dataclass


@dataclass
class Option:
    option_text: str
    is_correct: bool


@dataclass
class Question:
    question_id: int
    question_text: str
    options: list[Option]
