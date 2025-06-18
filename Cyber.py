import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

Cyber_Data = pd.read_excel("C:/Users/sande/Desktop/cyber_data.xlsx")
Cyber_Data.replace({'Yes': 1, 'No': 0}, inplace=True)


Cyber_Data['hacked'] = Cyber_Data['hacked'].apply(lambda x: 1 if x >= 5 else 0)

x = Cyber_Data[['SUS', 'SamePass', '2FA', 'Cyberknowledge', 'Workshop', 'urls', 'report', 'antivirus', 'pubwifi', 'strgpass']]
y = Cyber_Data['hacked']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Predicted:", y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

new_person = pd.read_excel("C:/Users/sande/Desktop/cyberpred.xlsx")
new_prediction = model.predict(new_person)
print("New Prediction:", new_prediction)