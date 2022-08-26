import logging
import logging.handlers
import pathlib
import sys
import typing


def create_logger(
    directory: pathlib.Path,
) -> logging.Logger:
    """
    Create custom application logger

    Args:
        directory: Storage path for log file
    """
    directory.mkdir(exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Log file handler
    log_file = directory.joinpath("application.log")
    log_format = logging.Formatter(
        "%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s"
    )

    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10485760, backupCount=10
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # STDOUT stream handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(log_format)
    logger.addHandler(stream_handler)

    # TODO: Add syslog handler

    return logger
