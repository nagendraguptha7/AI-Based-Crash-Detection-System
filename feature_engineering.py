import pandas as pd

df = pd.read_csv("labeled.csv")

# Rolling trends
df["cpu_trend"] = df["cpu"].rolling(5).mean()
df["ram_trend"] = df["ram"].rolling(5).mean()

# Network load
df["net_load"] = df["net_sent"] + df["net_recv"]

# Fill NaNs
df = df.bfill()

df.to_csv("features.csv", index=False)

print(df["failure"].value_counts())