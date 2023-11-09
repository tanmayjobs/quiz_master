
import json

from src.constants.messages import Messages
from src.constants.output_messages import OutputMessages
from src.constants.screen_texts import ScreenTexts
from src.constants.sql_queries import SQLQueries


def load_constants():

    with open("constants.yaml", "r") as constants_file:
        json_data = json.load(constants_file)
        SQLQueries(json_data["sql_queries"])
        ScreenTexts(json_data["screens"])
        OutputMessages(json_data["output"])
        Messages(json_data["message"])
