"""Core case conversion functions.

The conversion strategy is deliberately simple and predictable: the
input is split into words on underscores and on case boundaries
(lower-to-upper transitions). This covers the four target conventions
without needing to know which convention the input is written in.
"""

import re

_WORD_SPLIT_RE = re.compile(r"([A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+)")


def _split_words(identifier: str) -> list[str]:
    """Split an identifier into a list of lowercase words.

    The regex separates on case boundaries and underscores. Consecutive
    uppercase letters are treated as one word unless followed by a
    lowercase letter, in which case the last uppercase letter starts the
    next word. This matches common intuition for identifiers like
    "HTTPResponse" -> ["http", "response"].
    """
    # Replace underscores with spaces so they act as word separators.
    identifier = identifier.replace("_", " ")
    return [word.lower() for word in _WORD_SPLIT_RE.findall(identifier) if word.strip()]


def to_camel_case(identifier: str) -> str:
    """Convert an identifier to camelCase.

    Empty input returns an empty string.
    """
    words = _split_words(identifier)
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])


def to_pascal_case(identifier: str) -> str:
    """Convert an identifier to PascalCase.

    Empty input returns an empty string.
    """
    words = _split_words(identifier)
    return "".join(word.capitalize() for word in words)


def to_snake_case(identifier: str) -> str:
    """Convert an identifier to snake_case.

    Empty input returns an empty string.
    """
    return "_".join(_split_words(identifier))


def to_screaming_snake_case(identifier: str) -> str:
    """Convert an identifier to SCREAMING_SNAKE_CASE.

    Empty input returns an empty string.
    """
    return "_".join(word.upper() for word in _split_words(identifier))
