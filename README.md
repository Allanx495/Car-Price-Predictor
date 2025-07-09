# <img src="https://media1.giphy.com/media/RIYlDuzPKzRNiNkgHm/giphy.gif" width="170"/> Car Price Predictor

Objective:
Helping automobile buyers and sellers make smarter decisions by building a ML model based on essential features, and to bring overall transparency to the market.
--- 
This is a Flask-based web application that predicts the price of a car based on its specifications like max power, engine size, fuel type, brand, year, and number of seats. The backend model was trained using historical car data and deployed using `joblib` for real time predictions via a user-friendly web form.

---

## 📌 Features

- 🔍 Predicts estimated car price based on real input values
- 📊 Handles various car features including fuel type and brand
- 🌐 Interactive frontend built with HTML + Flask templating
- 💾 Uses a pre-trained machine learning model (`.pkl`)
- 🧪 Tested locally using VS Code + Flask dev server

---

## 🛠️ Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| Frontend      | HTML, CSS (inline)            |
| Backend       | Python, Flask                 |
| Model         | Scikit-learn, joblib, NumPy   |
| Dev Tools     | VS Code, Git, GitHub          |

---

## 📷 Demo

![Car Prediction Demo](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWo3Y24xM3J3eXY4amxoZ2R6OGFmYThraHZ1aWdyM3FxNHExaXd1ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/kRgu7N2qAkZRvZOt6E/giphy.gif)

---

## 🧪 Example Inputs

| Feature        | Example Value      |
|----------------|--------------------|
| Max Power (HP) | 132                |
| Engine Size    | 1800               |
| Year           | 2020               |
| Seats          | 5                  |
| Fuel Type      | Petrol             |
| Brand          | Toyota             |

🧠 **Estimated Output:** \$5,028 (based on model training data)

---

## 🚀 Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/Allanx495/Car-Price-Predictor.git
cd Car-Price-Predictor
