from flask import *
from pickle import load
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load saved model
with open("lung_cancer.pkl", "rb") as f:
    model = load(f)

@app.route("/")
def home():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get form data
        age = int(request.form["age"])
        gender = request.form["gender"].upper()
        smoking = int(request.form["smoking"])
        yellow_fingers = int(request.form["yellow_fingers"])
        anxiety = int(request.form["anxiety"])
        peer_pressure = int(request.form["peer_pressure"])
        chronic_disease = int(request.form["chronic_disease"])
        fatigue = int(request.form["fatigue"])
        allergy = int(request.form["allergy"])
        wheezing = int(request.form["wheezing"])
        alcohol = int(request.form["alcohol"])
        coughing = int(request.form["coughing"])
        short_breath = int(request.form["short_breath"])
        swallowing_diff = int(request.form["swallowing_diff"])
        chest_pain = int(request.form["chest_pain"])

        # Gender encoding
        gender_m = 1 if gender == "M" else 0

        # Arrange input in correct order
        features = [[
            age, smoking, yellow_fingers, anxiety, peer_pressure,
            chronic_disease, fatigue, allergy, wheezing,
            alcohol, coughing, short_breath, swallowing_diff,
            chest_pain, gender_m
        ]]

        # Prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100

        result = "YES" if prediction == 1 else "NO"

        return render_template("predict.html",
                               pred=f"LUNG CANCER: {result}",
                               prob=f"Probability: {probability:.2f}%")

if __name__ == "__main__":
    app.run(debug=True)
