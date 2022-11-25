from collections import namedtuple

URLParts = namedtuple(
    typename="URLParts",
    field_names=["scheme", "netloc", "path", "query", "fragment", "url"],
)
