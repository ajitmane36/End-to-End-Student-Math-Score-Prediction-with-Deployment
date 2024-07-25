import sys
import os

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException
import pandas as pd

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.joins('artifacts','train.csv')
    test_data_path:str=os.path.joins('artifacts','test.csv')
    raw_data_path:str=os.path.joins('artifacts','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try: