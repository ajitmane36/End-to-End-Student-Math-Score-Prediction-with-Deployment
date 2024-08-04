# End to End Data Science Project: Student Performance Indicator

## Overview
This project predicts students' math scores. It covers the entire process from data ingestion and transformation, to model training and deployment.

## Tools and Technologies
- **Conda**: For environment management.
- **Git**: Version control.
- **MySQL**: Database.
- **GitHub**: Code hosting.
- **DVC**: Data version control.
- **MLflow**: Model lifecycle management.
- **Flask**: Model Deployment.
- **Dagshub**: Data and experiment management.
- **AWS CodePipeline**: Continuous integration and delivery service for fast and reliable application and infrastructure updates.
- **AWS Elastic Beanstalk**: Easy-to-use service for deploying and scaling web applications and services.


## Project Structure
- **app.py**: Flask application script for deploying the model using flask and handling user inputs.
- **application.py**: Flask application script for deploying the model on AWS Elastic Beanstalk.
- **prediction_pipeline.py**: Scripts for making predictions based on user input.
- **data_ingestion.py**: Scripts for data ingestion and preprocessing.
- **data_transformation.py**: Scripts for data transformation.
- **model_trainer.py**: Scripts for model training.
- **notebooks**: Jupyter notebooks for analysis and model training experimentation.
- **utils.py**: Utility scripts.
- **requirements.txt**: Project dependencies.
- **artifacts**: Stores generated artifacts such as model performance reports and trained models.

## Setup Instructions
1. **Clone the repository:**
    ```sh
    git clone https://github.com/ajitmane36/mlproject.git
    cd mlproject
    ```

2. **Create a Conda environment:**
    ```sh
    conda create --name student-performance python=3.9
    conda activate student-performance
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```sh
    python app.py
    ```

5. **Navigate to the application in your browser:**
    ```sh
    # Home Page
    http://127.0.0.1:5000
    
    # Prediction Page
    http://127.0.0.1:5000/predictdata
    ```

## Usage
1. **Home Page:**
    - Access the home page to enter student data.
    - Submit the form to get predicted math scores.

2. **Prediction Pipeline:**
    - Handles user input and processes it through the trained model to provide predictions.

## Model Deployment
### Using Flask
![flask deployment](https://github.com/user-attachments/assets/f0f2c35e-22f2-4821-8cb8-18bc424c4704)

### Using AWS Elastic Beanstalk
![AWS Elastic Beanstalk deployment](https://github.com/user-attachments/assets/51b97933-c357-4575-8146-315ab2813982)
