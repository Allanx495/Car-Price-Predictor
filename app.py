from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('Car_price_app/new3_car_model.pkl')


# Predefined label encodings (must match your training data)
fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}  # adjust if needed
brand_map = {'Toyota': 0, 'Honda': 1, 'Hyundai': 2, 'Ford': 3, 'BMW': 4, 'Mercedes': 5}  # update based on your dataset

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        max_power = float(request.form['max_power'])
        engine = float(request.form['engine'])
        year = int(request.form['year'])
        seats = int(request.form['seats'])
        fuel = fuel_map.get(request.form['fuel'], -1)
        brand = brand_map.get(request.form['brand'], -1)

        features = np.array([[max_power, engine, year, seats, fuel, brand]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=f'Estimated Car Price: ${prediction:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
