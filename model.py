from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np

# Sample training data
data = {
    'Temperature': [25, 30, 28, 22, 20, 18, 27, 29, 23, 19],
    'Humidity': [70, 85, 60, 90, 80, 75, 65, 55, 95, 70],
    'Windy': [False, True, False, True, False, True, False, False, True, False],
    'Weather': ['Sunny', 'Rainy', 'Overcast', 'Rainy', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Rainy', 'Overcast']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Prepare features and target
X = df[['Temperature', 'Humidity', 'Windy']].replace({True: 1, False: 0})
y = df['Weather']

# Train Naïve Bayes model
model = GaussianNB()
model.fit(X, y)

def predict_weather(temperature, humidity, windy):
    """Predict weather based on input features."""
    input_data = np.array([[temperature, humidity, 1 if windy else 0]])
    prediction = model.predict(input_data)[0]  # Extract first element from array
    return str(prediction)  # Explicitly return as a plain string