import psutil
import pandas as pd
import time

rows = []

print("Collecting system data... Press Ctrl+C to stop.")

try:
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        net = psutil.net_io_counters()

        rows.append([
            time.time(),
            cpu,
            ram,
            disk,
            net.bytes_sent,
            net.bytes_recv
        ])

        time.sleep(1)

except KeyboardInterrupt:
    df = pd.DataFrame(rows, columns=[
        "time", "cpu", "ram", "disk", "net_sent", "net_recv"
    ])
    df.to_csv("raw_metrics.csv", index=False)
    print("Saved raw_metrics.csv with", len(df), "rows")