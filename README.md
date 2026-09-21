# SCREAMING_SNAKE Case Converter

Converts identifier strings between camelCase, PascalCase, snake_case, and SCREAMING_SNAKE_CASE.

```python
from screaming_snake_case_converter import (
    to_camel_case,
    to_pascal_case,
    to_snake_case,
    to_screaming_snake_case,
)

to_camel_case("hello_world")        # "helloWorld"
to_pascal_case("hello_world")       # "HelloWorld"
to_snake_case("helloWorld")         # "hello_world"
to_screaming_snake_case("helloWorld") # "HELLO_WORLD"
```

## Why this exists

Different programming communities use different identifier conventions, and moving code between languages or frameworks often requires renaming. This library does that one job with a single, consistent splitting rule: words are separated on underscores and on lower-to-upper case transitions. Consecutive uppercase letters are grouped as one word unless followed by a lowercase letter, so `HTTPResponse` becomes `http_response` rather than `h_t_t_p_response`.

## Edge cases

Input that contains digits splits them as separate words when they appear next to letters: `version2Value` becomes `version_2_value`. Repeated underscores are treated as a single separator. Empty input returns an empty string for all functions.
