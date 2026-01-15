import time
import psutil
import joblib
import pandas as pd
from collections import deque
from schema import FEATURES

model = joblib.load("crash_model.pkl")

cpu_hist = deque(maxlen=5)
ram_hist = deque(maxlen=5)

print("🔥 Live Crash Prediction Started")

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net = psutil.net_io_counters()

    cpu_hist.append(cpu)
    ram_hist.append(ram)

    cpu_trend = sum(cpu_hist) / len(cpu_hist)
    ram_trend = sum(ram_hist) / len(ram_hist)
    net_load = net.bytes_sent + net.bytes_recv

    row = pd.DataFrame([[
        cpu, ram, disk,
        net.bytes_sent, net.bytes_recv,
        cpu_trend, ram_trend, net_load
    ]], columns=FEATURES)

    prob = model.predict_proba(row)[0][1]

    if prob > 0.7:
        print(f"🔥 CRASH RISK {prob:.2f}")
    elif prob > 0.4:
        print(f"⚠️ WARNING {prob:.2f}")
    else:
        print(f"✅ SAFE {prob:.2f}")

    time.sleep(2)