import logging

from helpers.constants import Config


logging.basicConfig(
    level=logging.NOTSET,
    filename=Config.LOGS_FILE_PATH,
    filemode=Config.LOGS_FILEMODE,
    format=Config.LOGS_FORMAT,
    datefmt=Config.LOGS_DATEFMT,
)


logger = logging.getLogger()
