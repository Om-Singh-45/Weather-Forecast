from flask import Flask, render_template, request, redirect, url_for, send_file, make_response
from model import predict_weather
from database import init_db, save_prediction, get_prediction_history
import csv
import io
from datetime import datetime

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        windy = request.form['windy'] == 'True'
        
        # Predict weather using Naïve Bayes
        prediction = predict_weather(temperature, humidity, windy)
        
        # Save to database (prediction is already a string from predict_weather)
        save_prediction(temperature, humidity, windy, prediction)
        
        # Render result page with prediction
        return render_template('result.html', prediction=prediction)
    
    return render_template('index.html')

@app.route('/history')
def history():
    # Fetch prediction history from database
    predictions = get_prediction_history()
    return render_template('history.html', predictions=predictions)

@app.route('/export-csv')
def export_csv():
    # Fetch prediction history from database
    predictions = get_prediction_history()
    
    # Create a StringIO object for the CSV data
    si = io.StringIO()
    csv_writer = csv.writer(si)
    
    # Write header row
    csv_writer.writerow(['Temperature (°C)', 'Humidity (%)', 'Windy', 'Prediction', 'Timestamp'])
    
    # Write data rows
    for pred in predictions:
        # Convert windy boolean to Yes/No for better readability
        windy_status = 'Yes' if pred[2] else 'No'
        csv_writer.writerow([pred[0], pred[1], windy_status, pred[3], pred[4]])
    
    # Create response with CSV data
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f"attachment; filename=weather_predictions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    output.headers["Content-type"] = "text/csv"
    
    return output

if __name__ == '__main__':
    app.run(debug=True)