import sys
import os

# Add the src directory to the system path
# This allows you to import modules from the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging  # Import the logging module from the project

# Function to generate a detailed error message
def error_message_detail(error, error_detail: sys):
    """
    This function creates a detailed error message.

    Parameters:
    error (Exception): The original exception that was raised.
    error_detail (module): The sys module to get detailed error info.

    Returns:
    str: A formatted string with file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get the exception traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the file where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))  # Create a formatted error message
    return error_message  # Return the detailed error message

# Custom exception class for handling errors
class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        Initialize the custom exception with a detailed error message.

        Parameters:
        error_message (str): The original error message.
        error_details (module): The sys module to get detailed error info.
        """
        super().__init__(error_message)  # Initialize the base Exception class with the error message
        self.error_message = error_message_detail(error_message, error_details)  # Get and store the detailed error message
    
    def __str__(self):
        """
        Return the detailed error message when the exception is printed.

        Returns:
        str: The detailed error message.
        """
        return self.error_message  # Return the detailed error message
