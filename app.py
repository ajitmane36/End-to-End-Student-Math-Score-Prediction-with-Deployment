## We are checking logging and exception handling

import sys
import os

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        a=1/0 #error added
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)

# Now we can see error in log files 