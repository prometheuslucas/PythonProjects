import re


class Validator:
    """An abstract base class for validators."""

    def validate(self, value: str) -> bool:
        """Validate a value and return True if it is valid, False otherwise.

        Args:
            value (str): The value to validate.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        # This method should be implemented by subclasses
        raise NotImplementedError


class RegexValidator(Validator):
    """A validator that uses a regular expression pattern."""

    def __init__(self, pattern: str, description: str):
        """Initialize the RegexValidator with a pattern and a description.

        Args:
            pattern (str): The regular expression pattern to use.
            description (str): The word written definition of the pattern.
        """
        # Compile the pattern into a regex object
        self._regex = re.compile(pattern)
        # Assign the description to an attribute
        self._description = description

    def validate(self, value: str) -> bool:
        """Validate a value using the regex object and return True if it matches, False otherwise.

        Args:
            value (str): The value to validate.

        Returns:
            bool: True if the value matches the regex object, False otherwise.
        """
        # Use the regex object's match method
        return bool(self._regex.match(value))
