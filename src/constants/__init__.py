
import json

from constants.messages import Messages
from constants.output_messages import OutputMessages
from constants.screen_texts import ScreenTexts
from constants.sql_queries import SQLQueries


print("setting constants")

with open("constants/constants.yaml", "r") as constants_file:
    json_data = json.load(constants_file)
    SQLQueries(json_data["sql_queries"])
    ScreenTexts(json_data["screens"])
    OutputMessages(json_data["output"])
    Messages(json_data["message"])
