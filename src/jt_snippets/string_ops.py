from datetime import date, datetime
from typing import Union

from .enums import GroupFormat


def suffix_with_datetime(
    text: str,
    _datetime: Union[date, datetime],
    group_format: GroupFormat,
) -> str:
    """
    Suffix text with date/time values

    Args:
        text: Text to apply date/time suffix
        _datetime: Object date/datetime to suffix text
        group_format: Format of date/time suffix
    """
    collections = [text]

    if group_format.value == "SECOND":
        collections.append(_datetime.strftime(f"%Y%m%d_%H%M%S"))
    elif group_format.value == "MINUTE":
        collections.append(_datetime.strftime(f"%Y%m%d_%H%M"))
    elif group_format.value == "HOUR":
        collections.append(_datetime.strftime(f"%Y%m%d_%H"))
    elif group_format.value == "DAY":
        collections.append(_datetime.strftime(f"%Y%m%d"))
    elif group_format.value == "MONTH":
        collections.append(_datetime.strftime(f"%Y%m"))
    else:
        collections.append(_datetime.strftime(f"%Y"))

    return "_".join(collections)
