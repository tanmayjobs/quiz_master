import logging
import os

from helpers.constants import Config


logging.basicConfig(
    level=logging.NOTSET,
    filename=os.path.dirname(os.path.abspath(__file__)) + Config.LOGS_FILE_PATH,
    filemode=Config.LOGS_FILEMODE,
    format=Config.LOGS_FORMAT,
    datefmt=Config.LOGS_DATEFMT,
)


logger = logging.getLogger()
