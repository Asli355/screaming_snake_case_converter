"""Tests for case conversion functions."""

import unittest

from screaming_snake_case_converter import (
    to_camel_case,
    to_pascal_case,
    to_snake_case,
    to_screaming_snake_case,
)


class TestCaseConversions(unittest.TestCase):
    def test_camel_case_basic(self):
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")

    def test_camel_case_from_pascal(self):
        self.assertEqual(to_camel_case("HelloWorld"), "helloWorld")

    def test_camel_case_empty(self):
        self.assertEqual(to_camel_case(""), "")

    def test_camel_case_with_acronym(self):
        # Consecutive capitals are split only when followed by a lowercase.
        self.assertEqual(to_camel_case("HTTPResponse"), "httpResponse")

    def test_pascal_case_basic(self):
        self.assertEqual(to_pascal_case("hello_world"), "HelloWorld")

    def test_pascal_case_from_camel(self):
        self.assertEqual(to_pascal_case("helloWorld"), "HelloWorld")

    def test_pascal_case_empty(self):
        self.assertEqual(to_pascal_case(""), "")

    def test_snake_case_basic(self):
        self.assertEqual(to_snake_case("helloWorld"), "hello_world")

    def test_snake_case_from_screaming(self):
        self.assertEqual(to_snake_case("HELLO_WORLD"), "hello_world")

    def test_snake_case_empty(self):
        self.assertEqual(to_snake_case(""), "")

    def test_screaming_snake_case_basic(self):
        self.assertEqual(to_screaming_snake_case("hello_world"), "HELLO_WORLD")

    def test_screaming_snake_case_from_camel(self):
        self.assertEqual(to_screaming_snake_case("helloWorld"), "HELLO_WORLD")

    def test_screaming_snake_case_empty(self):
        self.assertEqual(to_screaming_snake_case(""), "")

    def test_digits_are_separate_words(self):
        # Digits are treated as their own word when surrounded by letters.
        self.assertEqual(to_snake_case("version2Value"), "version_2_value")

    def test_multiple_underscores_collapse(self):
        # Underscores act as separators; repeated separators do not create
        # empty words.
        self.assertEqual(to_snake_case("hello__world"), "hello_world")


if __name__ == "__main__":
    unittest.main()
