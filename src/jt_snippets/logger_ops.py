from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import stdout


def create_logger(
    directory: Path,
) -> Logger:
    """
    Create custom application logger

    Args:
        directory: Storage path for log file
    """
    directory.mkdir(exist_ok=True)

    logger = getLogger(__name__)
    logger.setLevel(DEBUG)

    # Log file handler
    log_file = directory.joinpath("application.log")
    log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

    file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=10)
    file_handler.setLevel(DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # STDOUT stream handler
    stream_handler = StreamHandler(stdout)
    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(log_format)
    logger.addHandler(stream_handler)

    # TODO: Add syslog handler

    return logger
