import sys
import os

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException
import pandas as pd
import pymysql

# Reading sensitive information from DOTENV file
from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


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