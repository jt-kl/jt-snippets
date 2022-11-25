from urllib.parse import urljoin, urlsplit, urlunparse

from .models import URLParts


def url_path_builder(
    paths: list[str],
):
    """
    URL Path Component Builder

    Args:
        paths: Collections of paths
    """
    sanitized = [i.strip("/") for i in paths if i]
    _paths = [i for x in sanitized for i in x.split("/") if i]

    return "/".join(_paths)


def url_builder(
    base_url: str,
    path: str,
) -> str:
    """
    URL Builder

    Args:
        base_url: Base URL
        path: URL path
    """
    result = urlsplit(base_url)
    revised = urljoin(result.path, path)

    parts = URLParts(
        scheme=result.scheme,
        netloc=result.netloc,
        path=revised,
        query="",
        fragment="",
        url="",
    )

    return urlunparse(parts)
