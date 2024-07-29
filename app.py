## We are checking logging and exception handling

import sys
import os

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestionConfig
from mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from mlproject.components.model_trainer import ModelTrainerConfig, ModelTrainer




if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        
        ## Data Ingestion
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        ## Data Transformation
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        
        ## Model Traning
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)