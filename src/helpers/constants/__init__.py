import os
import yaml

from helpers.constants.config import Config
from helpers.constants.log_text import LogText
from helpers.constants.messages import Messages
from helpers.constants.input_texts import InputTexts
from helpers.constants.numbers import Numbers
from helpers.constants.output_texts import OutputTexts
from helpers.constants.regex_patterns import RegexPatterns
from helpers.constants.screen_texts import ScreenTexts
from helpers.constants.sql_queries import SQLQueries
from helpers.constants.errors import Errors
from helpers.constants.strings import Strings

with open(os.path.dirname(os.path.abspath(__file__)) + "/constants.yaml",
          "r") as constants_file:
    yaml_data = yaml.safe_load(constants_file)

    Config(yaml_data["config"])
    Messages(yaml_data["messages"])
    InputTexts(yaml_data["inputs"])
    OutputTexts(yaml_data["outputs"])
    ScreenTexts(yaml_data["screens"])
    SQLQueries(yaml_data["sql_queries"])
    Errors(yaml_data["errors"])
    Strings(yaml_data["strings"])
    Numbers(yaml_data["numbers"])
    LogText(yaml_data["log_text"])
    RegexPatterns(yaml_data["regex_patterns"])
