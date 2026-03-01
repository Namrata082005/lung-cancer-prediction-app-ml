# 🫁 Lung Cancer Prediction – ML Deployment with Flask

_Predicting whether a person is at risk of lung cancer based on lifestyle habits and symptoms using a pre-trained ML model deployed as a web app._

---

## 📌 Table of Contents

- <a href="#overview">Overview</a>

- <a href="#business-problem">Project Goal</a>

- <a href="#dataset">Dataset</a>

- <a href="#tools--technologies">Tools & Technologies</a>

- <a href="#project-structure">Project Structure</a>

- <a href="#data-cleaning--preparation">Data Preparation</a>

- <a href="#exploratory-data-analysis-eda">Model Training & Analysis</a>

- <a href="#research-questions--key-findings">Key Features & Insights</a>

- <a href="#dashboard">Web Interface</a>

- <a href="#how-to-run-this-project">How to Run This Project</a>

- <a href="#final-recommendations">Future Improvements</a>

- <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project is a web application that predicts whether a person is at risk of lung cancer based on lifestyle habits and symptoms. Users fill out a simple form with factors like age, smoking history, and various symptoms to receive a prediction along with a probability score. The app is built with Flask for the backend and HTML/CSS for the frontend, serving as a demonstration of ML model deployment in a healthcare context.

---

<h2><a class="anchor" id="business-problem"></a>Project Goal</h2>

Early detection of lung cancer significantly improves survival rates. This project aims to:

- Deploy a trained ML classification model as an interactive web app

- Accept multiple symptom and lifestyle inputs for real-time prediction

- Return a clear YES/NO result with probability confidence

- Demonstrate end-to-end ML workflow from model loading to user interface

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Dataset contains binary symptom indicators and demographic data with target variable `LUNG_CANCER` (YES / NO)

- Pre-trained model saved as pickle file (`lung_cancer.pkl`)

- Features include: Age, Gender, Smoking, Yellow Fingers, Anxiety, Peer Pressure, Chronic Disease, Fatigue, Allergy, Wheezing, Alcohol Consuming, Coughing, Shortness of Breath, Swallowing Difficulty, Chest Pain

- Binary features encoded as 1 = No, 2 = Yes; Gender encoded as M = 1, F = 0

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python (Flask for web framework, Scikit-learn for ML model, NumPy for array handling)

- HTML/CSS (custom styled frontend with gradient UI)

- Pickle (for model serialization)

- GitHub

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

lung-cancer-prediction/

│

├── README.md

├── .gitignore

├── app.py # Main Flask application script

├── lung_cancer.pkl # Pre-trained ML model

│

├── templates/ # Folder for HTML templates

│ └── predict.html # UI template for the web form

---

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Preparation</h2>

- User inputs: Age (integer), Gender (M/F), and 13 binary symptom flags

- Gender encoding: M → 1, F → 0

- Features arranged in fixed order before passing to model for prediction

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Model Training & Analysis</h2>

**Assumptions from Training:**

- Model: Classification model (e.g., Logistic Regression / Random Forest) from Scikit-learn

- Features: 15 inputs covering demographics, habits, and symptoms

- No explicit EDA in this deployment; assume prior analysis showed:

&nbsp; - Smoking, chest pain, and wheezing are strong predictors of lung cancer risk

&nbsp; - Age and chronic disease contribute significantly to prediction probability

**Potential Issues:**

- No input validation on age range

- Dataset may have class imbalance between positive and negative cases

- Probabilities derived from model's predict_proba

---

<h2><a class="anchor" id="research-questions--key-findings"></a>Key Features & Insights</h2>

1\. **Input Features**: 15 lifestyle and symptom-based inputs for binary classification

2\. **Prediction Logic**: Real-time inference and probability calculation

3\. **User Experience**: Clean form with YES/NO prediction and confidence percentage

4\. **Insights**: Smoking, wheezing, and chest pain increase lung cancer probability

5\. **Limitations**: Binary output only; no multi-class severity prediction

---

<h2><a class="anchor" id="dashboard"></a>Web Interface</h2>

\- Flask-based web app shows:

&nbsp; - Input form for all 15 patient lifestyle and symptom fields

&nbsp; - Prediction result (LUNG CANCER: YES or LUNG CANCER: NO)

&nbsp; - Probability score showing confidence of the prediction

&nbsp; - Stylish design with purple gradient background and clean card layout

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1\. Clone the repository:

git clone https://github.com/yourusername/lung-cancer-prediction.git

Install dependencies:

Bashpip install flask scikit-learn numpy

Run the app:

Bashpython app.py

Open in browser:

Visit http://localhost:5000

Fill in the form and predict!

---

<h2><a class="anchor" id="final-recommendations"></a>Future Improvements</h2>

1\. Add input validation (e.g., age must be between 0–120)

2\. Display feature importance or risk factor breakdown

3\. Deploy to cloud (e.g., Render or Railway)

4\. Include model training notebook for full reproducibility

5\. Add patient history tracking with a database

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Name: Namrata Pokharkar

📧 Email: namratapokharkar20@gmail.com

🔗 LinkedIn: www.linkedin.com/in/namrata-pokharkar-862a55288
