import logging
from logging import INFO, DEBUG, WARN, CRITICAL, ERROR

from helpers.constants import Config

logging.basicConfig(
    level=logging.NOTSET,
    filename=Config.LOGS_FILE_PATH,
    filemode=Config.LOGS_FILEMODE,
    format=Config.LOGS_FORMAT,
    datefmt=Config.LOGS_DATEFMT,
)


class Logger:

    @staticmethod
    def log(lvl: int, msg: str, specific_name="server"):
        spc_logger = logging.getLogger(specific_name)
        spc_logger.log(lvl, msg)
