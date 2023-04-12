from logging import DEBUG, Formatter, Handler, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler, SysLogHandler
from pathlib import Path
from sys import stdout
from typing import Optional, TextIO


def create_console_stream_handler(
    stream: TextIO = stdout,
    level: int = DEBUG,
    format: Optional[str] = None,
) -> StreamHandler:  # type: ignore
    """
    Creates a console stream handler

    Args:
        stream: Logging output stream
        level: Logging level
        format: Log output format string
    """
    console_stream_handler = StreamHandler(stream)
    console_stream_handler.setLevel(level)

    if format:
        log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")
        console_stream_handler.setFormatter(log_format)

    return console_stream_handler


def create_syslog_handler(
    address: tuple[str, int] = ("localhost", 514),
    level: int = DEBUG,
    format: Optional[str] = None,
    **kwargs,
) -> SysLogHandler:
    """
    Creates a SysLog handler

    Args:
        address: Hostname and port number of SysLog host
        level: Logging level
        format: Log output format string
    """
    syslog_handler = SysLogHandler(
        address,
        **kwargs,
    )
    syslog_handler.setLevel(level)

    if format:
        log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")
        syslog_handler.setFormatter(log_format)

    return syslog_handler


def create_rotating_file_handler(
    directory: Path,
    filename: str = "application.log",
    level: int = DEBUG,
    format: Optional[str] = None,
    maximum_file_size: int = 10485760,
    maximum_file_count: int = 10,
    **kwargs,
) -> RotatingFileHandler:
    """
    Creates a rotating file handler

    Args:
        directory: Directory path to store log file
        filename: Desired log file name
        level: Logging level
        format: Log output format string
        maximum_file_size: Maximum file size before rolling over
        maximum_file_count: Maximum file count before rolling over
    """
    rotating_file_handler = RotatingFileHandler(
        directory.joinpath(filename),
        maxBytes=maximum_file_size,
        backupCount=maximum_file_count,
        **kwargs,
    )
    rotating_file_handler.setLevel(level)

    if format:
        log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")
        rotating_file_handler.setFormatter(log_format)

    return rotating_file_handler


def create_logger(
    name: Optional[str] = None,
    level: int = DEBUG,
    format: Optional[str] = None,
    handlers: list[Handler] = [],
) -> Logger:
    """
    Create custom application logger

    Args:
        name: Name of logger
        level: Logging level
        format: Log output format string
        handlers: Collection of handlers to add to logger
    """
    logger = getLogger(name)
    logger.setLevel(level)

    # Prevent logging from propagating to the root logger
    logger.propagate = False

    for handler in handlers:
        # Override log output format
        if format:
            log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")
            handler.setFormatter(log_format)

        logger.addHandler(handler)

    return logger
