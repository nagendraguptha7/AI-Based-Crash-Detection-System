# AI-Based System Crash Prediction

This project predicts **system crashes before they happen** using machine learning on real-time system telemetry.

## What it does
The model learns patterns that occur **before** a system failure by training on CPU, RAM, Disk, and Network usage.  
Crash labels are shifted backward in time so the model predicts **approaching failure**, not just failure.

## Features
- Live CPU, RAM, Disk, Network monitoring
- Time-shifted crash prediction
- Random Forest classifier
- Real-time risk scoring (Safe / Warning / Crash Risk)

## How it works
1. Historical system metrics are loaded from `server_metrics.csv`
2. Crash labels are shifted backward to create early-warning targets
3. A RandomForest model is trained
4. Live system data is streamed into the model
5. The model outputs crash probability every few seconds

## Run

### Install
```bash
pip install -r requirements.txt

train 
python train_model.py
