Project Overview
Cyber Risk Predictor uses logistic regression to classify individuals as at risk (1) or not at risk (0) of getting hacked. The prediction is based on how they answer questions related to cybersecurity behavior.

Dataset
The dataset is collected through a survey and contains the following features:

Feature	Description
SUS	Clicked suspicious links (1 = Yes, 0 = No)
SamePass	Reuses same password across accounts
2FA	Uses two-factor authentication
Cyberknowledge	Self-rated cybersecurity knowledge (1 to 10)
Workshop	Attended a cyber awareness session
urls	Checks URLs before clicking
report	Reports suspicious emails/messages
antivirus	Uses antivirus or security tools
pubwifi	Connects to public Wi-Fi without VPN
strgpass	Uses strong, unique passwords

Target Variable:

hacked: Created from a scale question (likelihood of getting hacked, 1 to 10).

If value >= 5 → 1 (At Risk)

Else → 0 (Not At Risk)

⚙️ Technologies Used
Python

Pandas

Scikit-learn

Excel (for dataset creation and preprocessing)

ML Model
Model Type: Logistic Regression

Library: sklearn.linear_model.LogisticRegression

Training/Test Split: 50% data for training, 50% for testing

Evaluation: Accuracy Score

How It Works
Load and preprocess the Excel data (Yes/No converted to 1/0).

Create a binary target (hacked) from a 1–10 scale.

Train a logistic regression model on the features.

Predict hacking risk for new data from another Excel file.

Display the prediction and model accuracy.

Example Output
vbnet
Copy
Edit
Predicted: [1 0 0 1 1 0 ...]
Accuracy: 0.78
New Prediction: [0]
📁 Files
cyber_data.xlsx — Main dataset

cyberpred.xlsx — New user data for prediction

cyber_risk_predictor.py — Python script containing the model

