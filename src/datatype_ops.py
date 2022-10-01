import decimal
import enum
import typing


def to_dictionary(
    _object: object,
) -> typing.Union[dict, None]:
    """
    Converts complex object to a dictionary data type

    Args:
        _object: Custom object to be converted
    """
    if isinstance(_object, dict):
        data = {}

        for key, value in _object.items():
            data[key] = to_dictionary(value)

        return data

    if hasattr(_object, "__dict__"):
        data = {}

        for key, value in _object.__dict__.items():
            if isinstance(value, dict):
                data[key] = to_dictionary(value)

            elif isinstance(value, list):
                for item in value:
                    to_dictionary(item)

            elif isinstance(value, enum.Enum):
                data[key] = value.value

            elif hasattr(value, "__dict__"):
                data[key] = to_dictionary(value)

            else:

                data[key] = value

        return data

    return None


def to_decimal(
    value: typing.Union[str, float, int],
    precision: typing.Union[int, None] = None,
) -> decimal.Decimal:
    """
    Converts the following object types below to decimal.Decimal
    - string
    - float
    - integer

    Args:
        value: Value to be converted
        precision: Decimal precision length
    """
    if precision:
        assert 0 < precision, f"Value of precision must be greater than 0"

        decimal.getcontext().prec = precision

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

    return decimal.Decimal(value)
