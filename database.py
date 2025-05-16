import mysql.connector
from datetime import datetime

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',        # Replace with your MySQL username
    'password': 'root', # Replace with your MySQL password
    'database': 'weather_db'
}

def init_db():
    """Initialize the database and create table if not exists."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS weather_db")
    cursor.execute("USE weather_db")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            temperature FLOAT NOT NULL,
            humidity FLOAT NOT NULL,
            windy BOOLEAN NOT NULL,
            prediction VARCHAR(50) NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def save_prediction(temperature, humidity, windy, prediction):
    """Save a prediction to the database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Ensure correct types
    temperature = float(temperature)  # Ensure float
    humidity = float(humidity)        # Ensure float
    windy = bool(windy)               # Ensure boolean (True/False)
    prediction = str(prediction)      # Ensure plain string
    
    query = "INSERT INTO predictions (temperature, humidity, windy, prediction) VALUES (%s, %s, %s, %s)"
    values = (temperature, humidity, windy, prediction)
    cursor.execute(query, values)
    
    conn.commit()
    cursor.close()
    conn.close()

def get_prediction_history():
    """Retrieve the last 10 predictions from the database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    query = "SELECT temperature, humidity, windy, prediction, timestamp FROM predictions ORDER BY timestamp DESC LIMIT 10"
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return results