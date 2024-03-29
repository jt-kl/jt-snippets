from decimal import Decimal

import pytest

from jt_snippets.datatype_ops import to_decimal

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
to_decimal_happy = [
    (
        dict(
            value="1751.95",
            places=4,
        ),
        dict(result=Decimal("1751.9500")),
    ),
    (
        dict(
            value=83.141592653,
            places=9,
        ),
        dict(result=Decimal("83.141592653")),
    ),
    (
        dict(value=5691),
        dict(result=Decimal("5691.00")),
    ),
    (
        dict(
            value="1,732.4923",
            places=4,
        ),
        dict(result=Decimal("1732.4923")),
    ),
]

# endregion: PyTest parametrized variables


class TestDataTypeOps:
    @pytest.mark.parametrize("payload, expect", to_decimal_happy)
    def test_happy_to_decimal(self, payload, expect):
        result = to_decimal(**payload)

        assert result == expect["result"]
