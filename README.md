
AI-Based System Crash Prediction

This project predicts system crashes before they happen using machine learning on real-time system telemetry.

Instead of detecting failures after they occur, this system learns the patterns that lead up to a crash and provides early-warning risk scores so action can be taken before the system goes down.


---

What it does

The system continuously monitors:

CPU usage

RAM usage

Disk usage

Network traffic


These signals are converted into time-series features and fed into a machine learning model that outputs a crash probability in real time.

The output is classified into:

SAFE

WARNING

CRASH RISK



---

How it works

The system is built as a full ML pipeline:

1. Data Collection

Real system telemetry is collected using psutil and stored in raw_metrics.csv.

2. Crash Labeling

A failure is defined when:

CPU > 95%

RAM > 95%

Disk > 95%


Crash labels are shifted backward in time so the model learns to predict approaching failures, not just the moment of crash.

This produces labeled.csv.

3. Feature Engineering

Additional features are generated:

Rolling CPU trend

Rolling RAM trend

Network load (sent + received)


This creates features.csv.

4. Model Training

An XGBoost classifier is trained on engineered features to learn pre-crash patterns.
The trained model is saved as crash_model.pkl.

5. Evaluation

The model is evaluated using a stratified train/test split and standard ML metrics:

Confusion matrix

Precision, recall, F1-score


6. Live Prediction

realtime_monitor.py streams live system data into the trained model and prints a real-time crash risk score every few seconds.


---

Project Structure

collector.py            → Collects real system telemetry  
label_failures.py       → Creates early-warning crash labels  
feature_engineering.py → Builds ML features  
train_model.py          → Trains XGBoost crash model  
evaluate.py             → Evaluates model accuracy  
realtime_monitor.py     → Live crash prediction  
requirements.txt        → Python dependencies


---

How to run

Install dependencies

pip install -r requirements.txt

Collect live data

python collector.py

Label crashes

python label_failures.py

Generate features

python feature_engineering.py

Train model

python train_model.py

Evaluate model

python evaluate.py

Run real-time crash prediction

python realtime_monitor.py


---

Why this is different

This is not a toy ML project.

This system:

Uses real operating system telemetry

Performs time-shifted failure labeling

Applies feature engineering on time-series data

Trains a production-grade ML model

Runs live inference on a real machine




