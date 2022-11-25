import pytest

from jt_snippets.internet_ops import url_builder

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources


# endregion: Mocked resources

# region: PyTest parametrized variables
url_builder_happy = [
    (
        dict(
            base_url="https://www.acme.com/api/v1/",
            path="login",
        ),
        dict(result="https://www.acme.com/api/v1/login"),
    )
]
# endregion: PyTest parametrized variables


class TestInternetOps:
    @pytest.mark.parametrize("payload, expect", url_builder_happy)
    def test_happy_url_builder(self, payload, expect):
        result = url_builder(**payload)

        assert result == expect["result"]
