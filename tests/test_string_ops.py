from datetime import date, datetime
from typing import Any
from unittest.mock import patch

import pytest

from jt_snippets.enums import GroupFormat
from jt_snippets.string_ops import pretty_print, suffix_with_datetime

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables

suffix_with_datetime_happy: list[Any] = [
    (
        dict(
            text="",
            _datetime=datetime(2023, 5, 11, 22, 5, 13),
            group_format=GroupFormat.SECOND,
        ),
        dict(
            result="20230511_220513",
        ),
    ),
    (
        dict(
            text="Hello_Mercury",
            _datetime=datetime(2023, 4, 27, 8, 19, 42),
            group_format=GroupFormat.SECOND,
        ),
        dict(
            result="Hello_Mercury_20230427_081942",
        ),
    ),
    (
        dict(
            text="Hello_Venus",
            _datetime=datetime(2023, 5, 11, 17, 57, 23),
            group_format=GroupFormat.MINUTE,
        ),
        dict(
            result="Hello_Venus_20230511_1757",
        ),
    ),
    (
        dict(
            text="Hello_Earth",
            _datetime=datetime(2023, 12, 24, 7, 18, 51),
            group_format=GroupFormat.HOUR,
        ),
        dict(
            result="Hello_Earth_20231224_07",
        ),
    ),
    (
        dict(
            text="Hello_Mars",
            _datetime=datetime(2023, 9, 2, 17, 1, 31),
            group_format=GroupFormat.DAY,
        ),
        dict(
            result="Hello_Mars_20230902",
        ),
    ),
    (
        dict(
            text="Hello_Jupiter",
            _datetime=datetime(2023, 1, 30, 3, 47, 7),
            group_format=GroupFormat.MONTH,
        ),
        dict(
            result="Hello_Jupiter_202301",
        ),
    ),
    (
        dict(
            text="Hello_Saturn",
            _datetime=datetime(2023, 10, 15, 15, 37, 4),
            group_format=GroupFormat.YEAR,
        ),
        dict(
            result="Hello_Saturn_2023",
        ),
    ),
    (
        dict(
            text="",
            _datetime=date(2023, 6, 28),
            group_format=GroupFormat.SECOND,
        ),
        dict(
            result="20230628_000000",
        ),
    ),
    (
        dict(
            text="Bye_Mercury",
            _datetime=date(2023, 9, 12),
            group_format=GroupFormat.SECOND,
        ),
        dict(
            result="Bye_Mercury_20230912_000000",
        ),
    ),
    (
        dict(
            text="Bye_Venus",
            _datetime=date(2023, 2, 27),
            group_format=GroupFormat.MINUTE,
        ),
        dict(
            result="Bye_Venus_20230227_0000",
        ),
    ),
    (
        dict(
            text="Bye_Earth",
            _datetime=date(2023, 11, 30),
            group_format=GroupFormat.HOUR,
        ),
        dict(
            result="Bye_Earth_20231130_00",
        ),
    ),
    (
        dict(
            text="Bye_Mars",
            _datetime=date(2023, 7, 24),
            group_format=GroupFormat.DAY,
        ),
        dict(
            result="Bye_Mars_20230724",
        ),
    ),
    (
        dict(
            text="Bye_Jupiter",
            _datetime=date(2023, 7, 9),
            group_format=GroupFormat.MONTH,
        ),
        dict(
            result="Bye_Jupiter_202307",
        ),
    ),
    (
        dict(
            text="Bye_Saturn",
            _datetime=date(2023, 2, 18),
            group_format=GroupFormat.YEAR,
        ),
        dict(
            result="Bye_Saturn_2023",
        ),
    ),
]

pretty_print_happy: list[Any] = [
    (
        {
            "content": {
                "id": "VYxa3asuAXq2gpxhFghmDtmzHrZtS9bm",
                "result": "deployed",
            },
            "width": 1000,
            "clear": True,
        },
        {},
    ),
    (
        {
            "content": {
                "id": "zx7ZyohQymqwFaMXF4wyg3xyRDL3xCd7",
                "result": "pending",
            },
            "width": 200,
        },
        {},
    ),
    (
        {
            "content": "deployed",
            "width": 200,
        },
        {},
    ),
]

# endregion: PyTest parametrized variables


class TestStringOps:
    @pytest.mark.parametrize("payload, expect", suffix_with_datetime_happy)
    @patch("os.system")
    def test_happy_suffix_with_datetime(self, mocked_func, payload, expect):
        result = suffix_with_datetime(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", pretty_print_happy)
    @patch("builtins.print")
    @patch("jt_snippets.string_ops.PrettyPrinter.pprint")
    @patch("jt_snippets.string_ops.system")
    def test_happy_pretty_print(self, mocked_system_func, mocked_pprint_func, mocked_print_func, payload, expect):
        pretty_print(**payload)

        if payload.get("clear"):
            mocked_system_func.assert_called()

        if isinstance(payload["content"], dict):
            mocked_print_func.assert_called()
        else:
            mocked_pprint_func.assert_called()
