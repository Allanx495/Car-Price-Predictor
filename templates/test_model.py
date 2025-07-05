import joblib

# Load the model
model = joblib.load('Car_price_app/new3_car_model.pkl')  # adjust path if needed

# Check number of input features expected
print("Model expects this many features:", model.n_features_in_)
