# 🫁 Lung Cancer Prediction – ML Deployment with Flask



_Predicting the likelihood of lung cancer based on lifestyle and symptom data using a pre-trained ML model deployed as a web app.\_



---



## 📌 Table of Contents



- \[Overview](#overview)

- \[Project Goal](#project-goal)

- \[Dataset](#dataset)

- \[Tools \& Technologies](#tools--technologies)

- \[Project Structure](#project-structure)

- \[Data Preparation](#data-preparation)

- \[Model Training & Analysis](#model-training--analysis)

- \[Key Features & Insights](#key-features--insights)

- \[Web Interface](#web-interface)

- \[How to Run This Project](#how-to-run-this-project)

- \[Future Improvements](#future-improvements)

- \[Author & Contact](#author--contact)



---



## Overview



This project is a web application that predicts whether a person is at risk of lung cancer based on lifestyle habits and symptoms. Users fill out a simple form with factors like age, smoking history, and various symptoms to receive a prediction along with a probability score. The app is built with Flask for the backend and HTML/CSS for the frontend, demonstrating an end-to-end ML model deployment pipeline.



---



## Project Goal



Early detection of lung cancer significantly improves survival rates. This project aims to:



- Deploy a trained ML classification model as an interactive web app

- Accept multiple symptom and lifestyle inputs for real-time prediction

- Return a clear YES/NO result with probability confidence

- Serve as a practical demonstration of ML deployment for healthcare use cases



---



## Dataset



- **Source**: Lung cancer dataset with binary symptom indicators and demographic data

- **Target Variable**: `LUNG\_CANCER` (YES / NO)

- **Features**: Age, Gender, Smoking, Yellow Fingers, Anxiety, Peer Pressure, Chronic Disease, Fatigue, Allergy, Wheezing, Alcohol Consuming, Coughing, Shortness of Breath, Swallowing Difficulty, Chest Pain

- **Encoding**: Binary features use 1 = No, 2 = Yes; Gender encoded as binary (M = 1, F = 0)

- Pre-trained model saved as `lung\_cancer.pkl`



---



## Tools & Technologies



- **Python** (Flask, Scikit-learn, NumPy)

- **HTML/CSS** (custom styled frontend with gradient UI)

- **Pickle** (model serialization)

- **GitHub** (version control)



---



## Project Structure

```

lung-cancer-prediction/

│

├── README.md

├── .gitignore

├── app.py                  # Main Flask application

├── lung\_cancer.pkl         # Pre-trained ML model

│

└── templates/

&nbsp;   └── predict.html        # UI form template

```



---



## Data Preparation



- **Inputs**: 15 features — 1 numeric (age), 1 categorical (gender), 13 binary symptom flags

- **Gender Encoding**: M → 1, F → 0

- **Binary Features**: Encoded as 1 (No) or 2 (Yes) to match training data format

- Features are arranged in a fixed order before passing to the model:

&nbsp; `\[age, smoking, yellow\_fingers, anxiety, peer\_pressure, chronic\_disease, fatigue, allergy, wheezing, alcohol, coughing, short\_breath, swallowing\_diff, chest\_pain, gender\_m]`



---



## Model Training & Analysis



**Model Used:** Classification model (e.g., Logistic Regression / Random Forest) trained on lung cancer symptom data



**Training Assumptions:**

- Binary classification: presence or absence of lung cancer

- Probability scores generated via `predict\_proba`

- Features selected based on medical relevance and dataset availability



**Potential Limitations:**

- No input validation on age range

- Dataset may have class imbalance (lung cancer cases vs. healthy)

- Model performance depends on training data quality



---



## Key Features & Insights



1. **15 Input Features** — covers demographics, habits, and symptoms

2. **Real-Time Prediction** — instant YES/NO result with probability %

3. **Gender Encoding** — handles M/F input and converts to numeric

4. **Probability Score** — shows confidence level of the prediction

5. **Clean UI** — gradient-themed, responsive form layout



---



## Web Interface



The Flask web app includes:

- A styled form collecting all 15 patient inputs

- A **Predict** button that sends data to the `/predict` route

- A result panel displaying:

&nbsp; - `LUNG CANCER: YES` or `LUNG CANCER: NO`

&nbsp; - `Probability: XX.XX%`



---



## How to Run This Project



1. **Clone the repository:**

```bash

&nbsp;  git clone https://github.com/yourusername/lung-cancer-prediction.git

&nbsp;  cd lung-cancer-prediction

```



2. **Install dependencies:**

```bash

&nbsp;  pip install flask scikit-learn numpy

```



3. **Add your model file:**

&nbsp;  - Place `lung\_cancer.pkl` in the root directory



4. **Run the app:**

```bash

&nbsp;  python app.py

```



5. **Open in browser:**

```

&nbsp;  http://localhost:5000

```

&nbsp;  Fill in the form and click \*\*Predict\*\*!



---



## Future Improvements



1. Add input validation (e.g., age must be between 0–120)

2. Display feature importance or risk factor breakdown

3. Deploy to cloud (Render, Railway, or Heroku)

4. Include model training notebook for full reproducibility

5. Add patient history tracking with a database

6. Improve accessibility and mobile responsiveness



---



## Author & Contact



**Name:** Namrata Pokharkar

📧 **Email:** namratapokharkar20@gmail.com

🔗 **LinkedIn:** [linkedin.com/in/namrata-pokharkar-862a55288](https://www.linkedin.com/in/namrata-pokharkar-862a55288)

