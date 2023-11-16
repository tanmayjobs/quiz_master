from dataclasses import dataclass


@dataclass
class QuizRecord:
    player_id: int
    player_name: str

    quiz_id: int
    quiz_name: str

    player_score: int
    total_score: int

    played_at: str = ""
