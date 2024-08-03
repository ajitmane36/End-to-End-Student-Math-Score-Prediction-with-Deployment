
import sys
import os

# Set the path to the src directory to import custom modules
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))

import pandas as pd  # Import Pandas for data manipulation
from mlproject.exception import CustomException  # Import CustomException for custom error handling
from mlproject.utils import load_object  # Import load_object utility function

# Define the PredictPipeline class for making predictions
class PredictPipeline:
    def __init__(self):
        pass

    # Method to make predictions
    def predict(self, features):
        try:
            # Define the paths to the model and preprocessor files
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            
            # Load the model and preprocessor objects
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            
            # Transform the input features using the preprocessor
            data_scaled = preprocessor.transform(features)
            
            # Make predictions using the loaded model
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)

# Define the CustomData class to handle input data
class CustomData:
    def __init__(self, gender: str, race_ethnicity: str, parental_level_of_education, lunch: str, test_preparation_course: str, reading_score: int, writing_score: int):
        # Initialize the attributes with the provided values
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    # Method to convert the input data to a DataFrame
    def get_data_as_data_frame(self):
        try:
            # Create a dictionary with the input data
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            
            # Convert the dictionary to a DataFrame and return it
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)