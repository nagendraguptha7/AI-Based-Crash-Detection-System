import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from schema import FEATURES

df = pd.read_csv("features.csv")

FEATURES = [
    "cpu","ram","disk","net_sent","net_recv",
    "cpu_trend","ram_trend","net_load"
]

X = df[FEATURES]
y = df["failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = joblib.load("crash_model.pkl")

pred = model.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

import json

report = classification_report(y_test, pred, output_dict=True)
with open("metrics.json", "w") as f:
    json.dump(report, f, indent=2)