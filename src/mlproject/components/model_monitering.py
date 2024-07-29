import sys
import os
import mlflow
import pandas as pd
import numpy as np
from evidently import *

from evidently.report import Report
from evidently.metric_plots import MetricPlot
from evidently.model_profile import Profile
from evidently.metric_functions import mean_absolute_error, mean_squared_error, r2_score
from evidently.model_profile.sections import DataDriftProfileSection, RegressionPerformanceProfileSection

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

            # Create an Evidently report
            report = Report()

            # Add data drift and regression performance sections to the report
            profile = Profile()
            profile.add(data=X_test, y_true=y_test, y_pred=y_pred)

            # Data drift section
            drift_section = DataDriftProfileSection()
            drift_section.add_train_data(X_train)
            drift_section.add_test_data(X_test)
            report.add_section(drift_section)

            # Regression performance metrics
            performance_section = RegressionPerformanceProfileSection()
            performance_section.add(y_true=y_test, y_pred=y_pred)
            report.add_section(performance_section)

            # Metrics to be displayed
            metrics = {
                "Mean Absolute Error (MAE)": mean_absolute_error(y_test, y_pred),
                "Root Mean Squared Error (RMSE)": np.sqrt(mean_squared_error(y_test, y_pred)),
                "R2 Score": r2_score(y_test, y_pred),
            }

            # Add metrics and profile to the report
            report.add_metric_plots(MetricPlot(metrics))
            report.add_profile(profile)

            # Save the report as an HTML file
            os.makedirs(os.path.dirname(self.model_monitoring_config.report_file_path), exist_ok=True)
            report.save(self.model_monitoring_config.report_file_path)

            logging.info(f"Model performance report saved to {self.model_monitoring_config.report_file_path}")
        
        except Exception as e:
            # Log and raise exceptions if report generation fails
            raise CustomException(e, sys)
