from InputString import InputString  # Import the InputString class from InputString.py


class OutputHandler:
    # This class has one responsibility: to display the output to the user

    def __init__(self):
        # This method initializes the class attributes
        self.output = None  # This attribute stores the output as a string

    def repeat_input(self, input: InputString):
        # This method repeats the user input and displays it to the standard output
        # The input parameter is an InputString object
        self.output = "You entered: " + str(input)  # Convert the input object to a string
        print(self.output)

    def display_error(self, error: Exception):
        # This method displays the error code to the standard output
        # The error parameter is an exception object
        self.output = "Error: " + str(error)  # Convert the error object to a string
        print(self.output)
