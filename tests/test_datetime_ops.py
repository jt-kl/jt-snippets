from datetime import date, datetime
from unittest.mock import patch

import pytest

import jt_snippets
import jt_snippets.datetime_ops
from jt_snippets.datetime_ops import (
    DateTimeFormat,
    export_datetime,
    get_weekdays,
    get_weekends,
    is_weekday,
    is_weekend,
    to_datetime,
)

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
export_datetime_happy = [
    (
        dict(
            _datetime=datetime(2022, 9, 1, 15, 30, 10),
            _format=DateTimeFormat.ISO8601,
        ),
        dict(
            result="2022-09-01T15:30:10",
        ),
    ),
    (
        dict(
            _datetime=datetime(2022, 8, 31, 9, 45, 25),
            _format=DateTimeFormat.RFC3339,
        ),
        dict(
            result="2022-08-31 09:45:25",
        ),
    ),
    (
        dict(
            _datetime=datetime(2022, 5, 29, 22, 15, 5),
            _format=f"%Y_%m_%d %H:%M:%S%z",
        ),
        dict(
            result="2022_05_29 22:15:05",
        ),
    ),
]

get_weekends_happy = [
    (
        dict(
            ranges=(
                date(2022, 9, 7),
                date(2022, 10, 1),
            )
        ),
        dict(
            result=[
                date(2022, 9, 10),
                date(2022, 9, 11),
                date(2022, 9, 17),
                date(2022, 9, 18),
                date(2022, 9, 24),
                date(2022, 9, 25),
            ]
        ),
    ),
    (
        dict(ranges=None),
        dict(
            result=[
                date(2022, 11, 5),
                date(2022, 11, 6),
                date(2022, 11, 12),
                date(2022, 11, 13),
                date(2022, 11, 19),
                date(2022, 11, 20),
                date(2022, 11, 26),
                date(2022, 11, 27),
            ]
        ),
    ),
]
get_weekends_sad = []

get_weekdays_happy = [
    (
        dict(
            ranges=(
                date(2022, 9, 7),
                date(2022, 10, 1),
            )
        ),
        dict(
            result=[
                date(2022, 9, 7),
                date(2022, 9, 8),
                date(2022, 9, 9),
                date(2022, 9, 12),
                date(2022, 9, 13),
                date(2022, 9, 14),
                date(2022, 9, 15),
                date(2022, 9, 16),
                date(2022, 9, 19),
                date(2022, 9, 20),
                date(2022, 9, 21),
                date(2022, 9, 22),
                date(2022, 9, 23),
                date(2022, 9, 26),
                date(2022, 9, 27),
                date(2022, 9, 28),
                date(2022, 9, 29),
                date(2022, 9, 30),
            ]
        ),
    ),
    (
        dict(ranges=None),
        dict(
            result=[
                date(2022, 10, 3),
                date(2022, 10, 4),
                date(2022, 10, 5),
                date(2022, 10, 6),
                date(2022, 10, 7),
                date(2022, 10, 10),
                date(2022, 10, 11),
                date(2022, 10, 12),
                date(2022, 10, 13),
                date(2022, 10, 14),
                date(2022, 10, 17),
                date(2022, 10, 18),
                date(2022, 10, 19),
                date(2022, 10, 20),
                date(2022, 10, 21),
                date(2022, 10, 24),
                date(2022, 10, 25),
                date(2022, 10, 26),
                date(2022, 10, 27),
                date(2022, 10, 28),
                date(2022, 10, 31),
            ]
        ),
    ),
]
get_weekends_sad = []

to_datetime_happy = [
    (
        dict(timestamp=1651382415),
        dict(result=datetime(2022, 5, 1, 5, 20, 15)),
    ),
    (
        dict(timestamp=1651558230.0),
        dict(result=datetime(2022, 5, 3, 6, 10, 30)),
    ),
    (
        dict(timestamp=1651841100000),
        dict(result=datetime(2022, 5, 6, 12, 45, 00)),
    ),
]
to_datetime_sad = []

is_weekday_happy = [
    (
        dict(
            day=datetime(2022, 6, 27, 14, 20, 15),
        ),
        dict(
            result=True,
        ),
    ),
    (
        dict(
            day=date(2022, 6, 28),
        ),
        dict(
            result=True,
        ),
    ),
]
is_weekday_sad = [
    (
        dict(
            day=datetime(2022, 6, 26, 9, 10, 5),
        ),
        dict(
            result=False,
        ),
    ),
    (
        dict(
            day=date(2022, 6, 25),
        ),
        dict(
            result=False,
        ),
    ),
]

is_weekend_happy = [
    (
        dict(
            day=datetime(2022, 7, 9, 18, 5, 0),
        ),
        dict(
            result=True,
        ),
    ),
    (
        dict(day=date(2022, 7, 10)),
        dict(
            result=True,
        ),
    ),
]
is_weekend_sad = [
    (
        dict(
            day=datetime(2022, 7, 12, 16, 0),
        ),
        dict(
            result=False,
        ),
    ),
    (
        dict(day=date(2022, 7, 13)),
        dict(
            result=False,
        ),
    ),
]

# endregion: PyTest parametrized variables


class TestDateTimeOps:
    @pytest.mark.parametrize("payload, expect", export_datetime_happy)
    def test_happy_export_datetime(self, payload, expect):
        result = export_datetime(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", get_weekends_happy)
    def test_happy_get_weekends(self, payload, expect):
        with patch(f"{jt_snippets.datetime_ops.__name__}.date", wraps=date) as mock:
            mock.today.return_value = date(2022, 11, 8)

            result = get_weekends(**payload)

            assert len(result) == len(expect["result"])

            for index, item in enumerate(result):
                assert item == expect["result"][index]

    @pytest.mark.parametrize("payload, expect", get_weekdays_happy)
    def test_happy_get_weekdays(self, payload, expect):
        with patch(f"{jt_snippets.datetime_ops.__name__}.date", wraps=date) as mock:
            mock.today.return_value = date(2022, 10, 15)

            result = get_weekdays(**payload)

            assert len(result) == len(expect["result"])
            for index, item in enumerate(result):
                assert item == expect["result"][index]

    @pytest.mark.parametrize("payload, expect", to_datetime_happy)
    def test_happy_to_datetime(self, payload, expect):
        result = to_datetime(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", is_weekday_happy)
    def test_happy_is_weekday(self, payload, expect):
        result = is_weekday(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", is_weekday_sad)
    def test_sad_is_weekday(self, payload, expect):
        result = is_weekday(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", is_weekend_happy)
    def test_happy_is_weekend(self, payload, expect):
        result = is_weekend(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", is_weekend_sad)
    def test_sad_is_weekend(self, payload, expect):
        result = is_weekend(**payload)

        assert result == expect["result"]
