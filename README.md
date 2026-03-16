# Salary Prediction Web App

A production-ready web application for predicting annual salaries in INR using machine learning, built with Python and Streamlit.

## Features
- Predict salary based on experience, education, job title, city, industry, and skills.
- Salary output as a range (±10%).
- Career insights dashboard with charts, suggestions, and positioning.

## Setup
1. Clone or download the `salary_app` directory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Train the model: `python train.py` (generates `salary_pipeline.joblib`).
4. Run the app: `streamlit run app.py`.

## File Structure
- `app.py`: Streamlit UI and insights display.
- `train.py`: Trains and saves the ML pipeline.
- `data.py`: Generates synthetic dataset.
- `insights.py`: Logic for career insights.
- `salary_pipeline.joblib`: Trained pipeline artifact.
- `requirements.txt`: Dependencies.
- `README.md`: This file.