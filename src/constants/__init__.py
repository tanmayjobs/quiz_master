
import yaml

from constants.log_text import LogText
from constants.messages import Messages
from constants.input_texts import InputTexts
from constants.numbers import Numbers
from constants.output_texts import OutputTexts
from constants.screen_texts import ScreenTexts
from constants.sql_queries import SQLQueries
from constants.errors import Errors
from constants.strings import Strings


with open("constants/constants.yaml", "r") as constants_file:
    yaml_data = yaml.safe_load(constants_file)

    Messages(yaml_data["messages"])
    InputTexts(yaml_data["inputs"])
    OutputTexts(yaml_data["outputs"])
    ScreenTexts(yaml_data["screens"])
    SQLQueries(yaml_data["sql_queries"])
    Errors(yaml_data["errors"])
    Strings(yaml_data["strings"])
    Numbers(yaml_data["numbers"])
    LogText(yaml_data["log_text"])
