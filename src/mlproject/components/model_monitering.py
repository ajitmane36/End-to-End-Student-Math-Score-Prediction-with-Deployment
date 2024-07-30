import sys
import os
import mlflow
import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently import Report
from evidently.metrics import DataDriftMetric, RegressionPerformanceMetric

# Set the path to the src directory
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

from mlproject.logger import logging
from mlproject.exception import CustomException
from dataclasses import dataclass

@dataclass
class ModelMonitoringConfig:
    # Path to save the model performance report
    report_file_path = os.path.join('artifacts', 'model_performance_report.html')

class ModelMonitoring:
    def __init__(self):
        self.model_monitoring_config = ModelMonitoringConfig()

    def load_model(self):
        """
        Load the model from MLflow using the specified run ID.
        """
        try:
            # Load the model from MLflow using the run ID
            model_uri = "runs:/900dfa74ea4d485e8a8af5765607cbaf/model"  # Replace <run_id> with the actual run ID
            model = mlflow.sklearn.load_model(model_uri)
            logging.info(f"Model loaded from MLflow run: {model_uri}")
            return model
        except Exception as e:
            # Log and raise exceptions if model loading fails
            raise CustomException(e, sys)

    def generate_report(self, train_path, test_path):
        """
        Generate a report to monitor model performance and data drift.
        """
        try:
            # Load the training and test datasets
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Loaded training and test datasets.")

            # Split data into features (X) and target (y)
            target_column_name = "math_score"  # Replace with your target column name
            X_train = train_df.drop(columns=[target_column_name], axis=1)
            y_train = train_df[target_column_name]
            X_test = test_df.drop(columns=[target_column_name], axis=1)
            y_test = test_df[target_column_name]
            logging.info("Split data into features and target.")

            # Load the pre-trained model
            model = self.load_model()

            # Make predictions on the test set
            y_pred = model.predict(X_test)
            logging.info("Generated predictions for the test set.")

            # Define the column mapping
            column_mapping = ColumnMapping(
                target=target_column_name,
                prediction="prediction"
            )

            # Create an Evidently report
            report = Report(metrics=[
                DataDriftMetric(),
                RegressionPerformanceMetric()
            ])

            # Add the predictions to the test data
            test_df["prediction"] = y_pred

            # Run the report
            report.run(reference_data=train_df, current_data=test_df, column_mapping=column_mapping)

            # Save the report as an HTML file
            os.makedirs(os.path.dirname(self.model_monitoring_config.report_file_path), exist_ok=True)
            report.save_html(self.model_monitoring_config.report_file_path)

            logging.info(f"Model performance report saved to {self.model_monitoring_config.report_file_path}")
        
        except Exception as e:
            # Log and raise exceptions if report generation fails
            raise CustomException(e, sys)
