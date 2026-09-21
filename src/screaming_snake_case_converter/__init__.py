"""Convert between common identifier case conventions.

This package provides functions for converting identifiers between
camelCase, PascalCase, snake_case, and SCREAMING_SNAKE_CASE.
"""

from .core import (
    to_camel_case,
    to_pascal_case,
    to_snake_case,
    to_screaming_snake_case,
)

__all__ = [
    "to_camel_case",
    "to_pascal_case",
    "to_snake_case",
    "to_screaming_snake_case",
]
