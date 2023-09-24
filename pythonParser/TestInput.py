import unittest
from InputString import InputString, InvalidInputError
from Validator import Validator, RegexValidator


class TestInput(unittest.TestCase):
    """A test class for the InputString and Validator classes."""

    def setUp(self):
        """Set up a regex validator with a specific pattern and description."""
        self.pattern = r"^[a-zA-ZäöüÄÖÜßáéíóúÁÉÍÓÚñÑ,.?!;:'\"()\s-]+$"
        self.description = "a strings with regular punctuation and characters of english, german and spanish"
        self.validator = RegexValidator(self.pattern, self.description)

    def test_input_string_valid(self):
        """Test that an input string with a valid value is created successfully."""
        input_string = InputString("Hello world!", self.validator)
        self.assertEqual(input_string._value, "Hello world!")
        self.assertEqual(input_string._validator, self.validator)

    def test_input_string_invalid(self):
        """Test that an input string with an invalid value raises an exception."""
        with self.assertRaisesRegex(InvalidInputError,
                                    f"'こんにちは世界!' is not valid because it does not match {self.description!r}."):
            input_string = InputString("こんにちは世界!", self.validator)

    def test_regex_validator_valid(self):
        """Test that a regex validator validates a valid value correctly."""
        self.assertTrue(self.validator.validate("Hello world!"))

    def test_regex_validator_invalid(self):
        """Test that a regex validator validates an invalid value correctly."""
        self.assertFalse(self.validator.validate("こんにちは世界!"))

    def test_regex_validator_invalid_pattern(self):
        """Test that a regex validator with an invalid pattern raises an exception."""
        with self.assertRaises(re.error):
            validator = RegexValidator("[invalid", "an invalid pattern")


if __name__ == "__main__":
    unittest.main()
