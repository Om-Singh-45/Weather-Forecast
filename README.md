# Weather Prediction Website

A Flask-based web application that uses Naïve Bayes to predict weather conditions (Sunny, Rainy, Overcast) based on user inputs (Temperature, Humidity, Windy). The project includes a MySQL database to store predictions and a history page to view past predictions.

## Features
- Predict weather using Naïve Bayes algorithm
- User-friendly form with Bootstrap UI
- MySQL database to log predictions
- History page with tabular data
- Modular and well-commented code

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure MySQL in `database.py` with your credentials
3. Run the app: `python app.py`

## Tech Stack
- Backend: Python Flask
- Frontend: HTML, CSS (Bootstrap), minimal JavaScript
- ML: Scikit-learn (Naïve Bayes)
- Database: MySQL