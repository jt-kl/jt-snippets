from collections import namedtuple
from urllib.parse import urljoin, urlparse, urlsplit, urlunparse, urlunsplit

from .models import URLParts


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
