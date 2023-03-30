from jt_snippets.models import URLParts

# region: Helper methods
# endregion: Helper methods

# region: Mocked resources
# endregion: Mocked resources

# region: PyTest parametrized variables
# endregion: PyTest parametrized variables


class TestModels:
    def test_happy_URLParts_model(self):
        for field in ["scheme", "netloc", "path", "query", "fragment", "url"]:
            assert hasattr(URLParts, field)
