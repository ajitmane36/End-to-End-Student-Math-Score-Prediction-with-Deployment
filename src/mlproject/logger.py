import logging
import os
from datetime import datetime

# log file name format in datetime with log file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating path for file in 
# current working directory with logs folder
log_path=os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating folder to store logs
os.makedirs(log_path, exist_ok=True)

# Combining file and path
LOG_FILE_PATH=os.path.join(log_path, LOG_FILE)

# Configuring log by format 
# like time, line number, level and error message
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    )

# Also you can use logging.ERROR, logging.warnings etc which is required

