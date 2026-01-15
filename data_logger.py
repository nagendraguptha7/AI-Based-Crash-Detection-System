import psutil
import time
import csv
import os

FILE = "telemetry_log.csv"

# Write header if file doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time","cpu","ram","disk","net_sent","net_recv"])

print("📡 Logging system telemetry. Press CTRL+C to stop.")

prev_net = psutil.net_io_counters()

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net = psutil.net_io_counters()

    sent = net.bytes_sent - prev_net.bytes_sent
    recv = net.bytes_recv - prev_net.bytes_recv
    prev_net = net

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), cpu, ram, disk, sent, recv])

    print(f"CPU:{cpu} RAM:{ram} DISK:{disk} NET↑:{sent} NET↓:{recv}")

    time.sleep(2)