# Import class and dependancies

import sys
import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# Set the path to the src directory to import custom modules
sys.path.append(os.path.abspath("C:\\Users\\ajitm\\.vscode\\data\\mlproject\\src"))


from sklearn.preprocessing import StandardScaler
from mlproject.pipelines.prediction_pipeline import CustomData, PredictPipeline  # Import custom data and prediction pipeline classes

# Create a Flask application instance
application = Flask(__name__)

# Assign the Flask app instance to a variable for ease of use
app = application

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template when accessing the root URL

# Define the route for predicting data points
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')  # Render the home.html template for GET requests
    else:
        # Create an instance of CustomData with form data
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        # Convert the data to a DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)  # Print the DataFrame for debugging
        print("Before Prediction")  # Debug message

        # Create an instance of PredictPipeline
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")  # Debug message

        # Make predictions using the predict pipeline
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")  # Debug message

        # Render the home.html template with prediction results
        return render_template('home.html', results=round(results[0],0))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Run the app on all available network interfaces
    # hit in browser 127.0.0.1:5000--> Home Page
    # 127.0.0.1:5000/predictdata --> Prediction Page