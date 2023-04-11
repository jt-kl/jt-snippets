from logging import INFO, Formatter, Logger, StreamHandler, getLogger
from sys import stdout

from ._version import VERSION

log_format = Formatter("%(asctime)s|%(levelname)-8s|%(module)s:%(funcName)s:%(lineno)d - %(message)s")

stream_handler = StreamHandler(stdout)
stream_handler.setLevel(INFO)
stream_handler.setFormatter(log_format)

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(stream_handler)
