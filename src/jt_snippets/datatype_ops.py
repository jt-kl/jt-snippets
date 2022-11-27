from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Union


def to_dictionary(
    _object: object,
    reserved: bool = False,
    _sorted: bool = False,
) -> Union[dict, None]:
    """
    Converts complex object to a dictionary data type

    Args:
        _object: Custom object to be converted
        reserved: Parse for reserved words
        _sorted: Sort dictionary by keys
    """
    reserved_keywords = ["from", "class"]

    if isinstance(_object, dict):
        data = {}

        for key, value in _object.items():
            data[key] = to_dictionary(value)

        if _sorted:
            return dict(sorted(data.items()))

        return data

    if hasattr(_object, "__dict__"):
        data = {}

        for key, value in _object.__dict__.items():
            if isinstance(value, dict):
                data[key] = to_dictionary(value)

            elif isinstance(value, list):
                if not value:
                    data[key] = value

                for item in value:
                    to_dictionary(item)

            elif isinstance(value, datetime):
                data[key] = value.isoformat("T") + "Z"

            elif isinstance(value, Enum):
                data[key] = value.value

            elif hasattr(value, "__dict__"):
                data[key] = to_dictionary(value)

            else:
                if reserved and key.endswith("_") and key.rstrip("_") in reserved_keywords:
                    data[key.rstrip("_")] = value
                else:
                    data[key] = value

        if _sorted:
            return dict(sorted(data.items()))

        return data

    return None


def to_decimal(
    value: Union[str, float, int],
) -> Decimal:
    """
    Converts the following object types below to Decimal
    - string
    - float
    - integer

    Args:
        value: Value to be converted

    Example:
        to_decimal(3.142)
        to_decimal(1,432,423.31)
    """
    if isinstance(value, float):
        value = str(value)

    if isinstance(value, int):
        value = str(value)

    # Sanitize separator values from prettified value
    # Examples:
    #   3,948,157.00 to 3948157.00
    #   4,000.61 to 4000.61
    for character, replacement in [(",", "")]:
        value = value.replace(character, replacement)

    return Decimal(value)
