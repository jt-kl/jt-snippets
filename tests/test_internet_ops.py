import pytest

from jt_snippets.internet_ops import url_builder, url_path_builder

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

url_path_builder_happy = [
    (
        dict(paths=["v1/exchange/", "symbol/", "expiry/range/start", "time/"]),
        dict(result="v1/exchange/symbol/expiry/range/start/time"),
    ),
    (
        dict(paths=["v3/api", "", "emails", "labels/update"]),
        dict(result="v3/api/emails/labels/update"),
    ),
    (
        dict(paths=["v1/credentials", "/user/", "", "/", "reset"]),
        dict(result="v1/credentials/user/reset"),
    ),
]
# endregion: PyTest parametrized variables


class TestInternetOps:
    @pytest.mark.parametrize("payload, expect", url_builder_happy)
    def test_happy_url_builder(self, payload, expect):
        result = url_builder(**payload)

        assert result == expect["result"]

    @pytest.mark.parametrize("payload, expect", url_path_builder_happy)
    def test_happy_url_path_builder(self, payload, expect):
        result = url_path_builder(**payload)

        assert result == expect["result"]
