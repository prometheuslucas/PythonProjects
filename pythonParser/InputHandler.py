# This file contains the InputHandler class that handles the user input

from InputString import InputString, InvalidInputError
# Import the InputString class and the InvalidInputError exception from InputString.py
from Validator import Validator


# Import the Validator abstract base class from Validator.py


class InputHandler:
    # This class has one responsibility: to get and validate the user input

    def __init__(self, validator: Validator):
        # This method initializes the class attributes
        # The validator parameter is a Validator object that will be used to validate the input
        self.input = None  # This attribute stores the user input as an InputString object
        self.error = None  # This attribute stores any error that occurs during validation as an exception
        self.validator = validator  # This attribute stores the validator object

    def get_input(self) -> InputString:
        # This method gets the user input from the standard input and returns it as an InputString object
        try:
            self.input = InputString(
                input("Please enter a string: "),
                self.validator)  # Try to create an InputString object from the user input and pass the validator object
            return self.input
        except InvalidInputError as e:  # If an exception is raised
            self.error = e  # Store the exception in the error attribute
            return None
