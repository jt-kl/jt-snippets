from collections import namedtuple

URLParts = namedtuple(
    "URLParts",
    ["scheme", "netloc", "path", "query", "fragment", "url"],
)
