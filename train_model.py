import pandas as pd
from xgboost import XGBClassifier
import joblib
from schema import FEATURES

df = pd.read_csv("features.csv")

X = df[FEATURES]
y = df["failure"]

pos = (y == 1).sum()
neg = (y == 0).sum()
scale = neg / pos

model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    scale_pos_weight=scale,
    eval_metric="logloss"
)

model.fit(X, y)

joblib.dump(model, "crash_model.pkl")
print("🚀 Model trained")