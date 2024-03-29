from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Union


def is_compound_reserved(
    key: str,
) -> bool:
    """
    Check for keys that are sub-set of Python reserved words

    Args:
        key: Name of key
    """
    reserved_words = [
        "False",
        "def",
        "if",
        "raise",
        "None",
        "del",
        "import",
        "return",
        "True",
        "elif",
        "in",
        "try",
        "and",
        "else",
        "is",
        "while",
        "as",
        "except",
        "lambda",
        "with",
        "assert",
        "finally",
        "nonlocal",
        "yield",
        "break",
        "for",
        "not",
        "class",
        "from",
        "or",
        "continue",
        "global",
        "pass",
    ]
    custom_words = [
        "type",
        "self",
        "format",
        "reversed",
    ]

    reserved_words.extend(custom_words)

    if key.endswith("_"):
        splits = key.split("_")
        if len(splits) == 2:
            if splits[0] in reserved_words:
                return True

    return False


def dictionary_factory(
    data: list[tuple[str, Any]],
) -> dict[str, Any]:
    """
    Conversion factory for dataclasses.asdict()

    Args:
        data: Data feed from dataclasses.asdict()
    """
    converted = dict()

    for key, value in data:
        key = key.strip("_") if is_compound_reserved(key) else key

        if isinstance(value, datetime) or isinstance(value, date):
            converted[key] = value.isoformat()

        elif isinstance(value, Enum):
            converted[key] = value.value

        else:
            converted[key] = value

    return converted


def to_dictionary(
    _object: object,
    reserved: bool = False,
    _sorted: bool = False,
):
    """
    Converts complex object to a dictionary data type

    Args:
        _object: Custom object to be converted
        reserved: Parse for reserved words
        _sorted: Sort dictionary by keys
    """
    reserved_keywords = ["from", "class"]

    if hasattr(_object, "__dict__"):
        data = {}

        for key, value in _object.__dict__.items():
            if isinstance(value, Enum):
                data[key] = value.value

            elif isinstance(value, datetime):
                data[key] = value.isoformat("T") + "Z"

            elif hasattr(value, "__dict__"):
                data[key] = to_dictionary(value, reserved, _sorted)

            elif isinstance(value, dict):
                data[key] = to_dictionary(value, reserved, _sorted)

            elif isinstance(value, list):
                if not value:
                    data[key] = value
                else:
                    data[key] = [to_dictionary(item, reserved, _sorted) for item in value]

            else:
                if reserved and key.endswith("_") and key.rstrip("_") in reserved_keywords:
                    data[key.rstrip("_")] = value
                else:
                    data[key] = value

        if _sorted:
            return dict(sorted(data.items()))

        return data

    elif isinstance(_object, dict):
        return _object

    # Accounts for list of simple native objects: strings, integers, floats
    # and decimals
    conditions = (
        isinstance(_object, dict),
        isinstance(_object, list),
        isinstance(_object, str),
        isinstance(_object, int),
        isinstance(_object, float),
        isinstance(_object, Decimal),
    )

    if any(conditions):
        return _object

    raise Exception(f"Object conversion error: {_object}")


def to_decimal(
    value: Union[str, float, int],
    places: int = 2,
) -> Decimal:
    """
    Converts the following object types below to Decimal
    - string
    - float
    - integer

    Args:
        value: Value to be converted
        places: Format values with required decimal places

    Example:
        to_decimal(3.142)
        to_decimal(1,432,423.31)
    """
    exponent = Decimal("10") ** -abs(places)

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

    return Decimal(value).quantize(exponent)


def prettify_json():
    """
    Prettify JSON
    """
    pass
