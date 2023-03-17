from datetime import date, datetime
from json import dumps
from pprint import PrettyPrinter
from typing import Any, Union

from .enums import GroupFormat


def suffix_with_datetime(
    text: str,
    _datetime: Union[date, datetime],
    group_format: GroupFormat = GroupFormat.SECOND,
) -> str:
    """
    Suffix text with date/time values

    Args:
        text: Text to apply date/time suffix
        _datetime: Object date/datetime to suffix text
        group_format: Desired format of date/time suffix
    """
    collections = []

    if text:
        collections.append(text)

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


def pretty_print(
    content: Union[dict[str, Any], str],
    width: int = 5000,
):
    """
    Pretty print content

    Args:
        content: Content to pretty print
        width: Maximum line width before wrapping
    """
    pp = PrettyPrinter(
        indent=2,
        width=width,
    )

    if isinstance(content, dict):
        print(dumps(content))
    else:
        pp.pprint(content)
