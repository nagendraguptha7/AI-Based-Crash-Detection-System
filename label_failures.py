import pandas as pd

df = pd.read_csv("raw_metrics.csv")

# Define real crash conditions
df["failure"] = 0

crash_condition = (
    (df["cpu"] > 85) |
(df["ram"] > 90) |
(df["disk"] > 95)
)

df.loc[crash_condition, "failure"] = 1

# Shift crashes backwards (early warning)
for i in df[df["failure"] == 1].index:
    df.loc[max(i-30,0):i, "failure"] = 1

df.to_csv("labeled.csv", index=False)

print(df["failure"].value_counts())