from Validator import Validator


class InvalidInputError(Exception):
    # This class defines a custom exception for invalid input
    def __init__(self, message):
        # This method initializes the exception with a message
        super().__init__(message)


class InputString:
    # This class defines a domain primitive for the input string

    def __init__(self, value: str, validator: Validator):
        # This method initializes the input string with a value and a validator
        # The value parameter is a string
        # The validator parameter is a Validator object that will be used to validate the value
        # Validate the value using the validator object
        if not validator.validate(value):
            # If the value is not valid, raise an exception with the value and the description
            raise InvalidInputError(f"{value} is not valid because it does not match {validator._description}")
        # Assign the value and validator to attributes
        self._value = value
        self._validator = validator

    def __str__(self) -> str:
        """Return the string representation of the InputString.

        Returns:
            str: The value of the input string.
        """
        return self._value

    def __eq__(self, other: object) -> bool:
        """Check if the InputString is equal to another object.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the other object is also an InputString with the same value, False otherwise.
        """
        # Check if the other object is also an InputString
        if isinstance(other, InputString):
            # Compare the values
            return self._value == other._value
        # Otherwise return False
        return False

    def __hash__(self) -> int:
        """Return the hash value of the InputString.

        Returns:
            int: The hash value of the input string.
        """
        # Use the built-in hash function on the value
        return hash(self._value)
