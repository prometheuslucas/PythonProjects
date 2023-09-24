from InputHandler import InputHandler
from OutputHandler import OutputHandler
from Validator import RegexValidator

# Define the pattern and description for the regex validator
pattern = r"^[a-zA-ZäöüÄÖÜßáéíóúÁÉÍÓÚñÑ,.?!;:'\"()\s-]+$"
description = "a strings with regular punctuation and characters of english, german and spanish"

# Create an instance of the regex validator with the pattern and description
validator = RegexValidator(pattern, description)

# Create an instance of InputHandler class and pass the validator object
input_handler = InputHandler(validator)

# Create an instance of OutputHandler class
output_handler = OutputHandler()

# Get the user input from InputHandler
user_input = input_handler.get_input()

# Check if there is any error in the input
error = input_handler.error

# If there is no error, repeat the input using OutputHandler
if not error:
    output_handler.repeat_input(user_input)
# If there is an error, display the error code using OutputHandler
else:
    output_handler.display_error(error)
