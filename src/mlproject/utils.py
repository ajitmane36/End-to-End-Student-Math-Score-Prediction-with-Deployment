import sys
import os

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException

import numpy as np
import pandas as pd
import pickle
import pymysql

# Reading sensitive information from DOTENV file
from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

# For data ingestion from MYSQL database
def read_sql_data():
    logging.info("Reading SQL database started")
    
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        
        logging.info("Connection established",mydb)
        df=pd.read_sql_query('SELECT * FROM students',mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex)
    
    
# Saving file in desired path in pickle format 
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)