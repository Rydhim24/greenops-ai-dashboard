import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data/cloud_usage_dataset.csv", parse_dates=["date"])

# Explore
print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nNull Values:")
print(df.isnull().sum())

# Remove nulls if any
df = df.dropna()

# Cost Analysis
print("\nTotal Cost:")
print(df["cost_usd"].sum())

daily_cost = df.groupby("date")["cost_usd"].sum().mean()
print("\nAverage Daily Cost:")
print(daily_cost)

# CO2e Calculation
df["co2e_kg"] = (
    (df["cpu_hours"] * 0.0002)
    + (df["storage_gb"] * 0.00006 / 30)
    + (df["data_transfer_gb"] * 0.001)
)

print("\nTotal CO2e:")
print(df["co2e_kg"].sum())

print("\nCO2e by Service:")
print(df.groupby("service_type")["co2e_kg"].sum())

print("\nCO2e by Team:")
print(df.groupby("team")["co2e_kg"].sum())

# Daily CO2e Chart
daily = df.groupby("date")["co2e_kg"].sum()

plt.figure(figsize=(8,5))
daily.plot()
plt.title("Daily CO2e")
plt.ylabel("kg CO2e")
plt.savefig("data/daily_co2e.png")
plt.close()

# Region Chart
region = df.groupby("region")["co2e_kg"].sum()

plt.figure(figsize=(8,5))
region.plot(kind="bar")
plt.title("CO2e by Region")
plt.ylabel("kg CO2e")
plt.savefig("data/co2e_by_region.png")
plt.close()

# Save enriched dataset
df.to_csv("data/cloud_usage_enriched.csv", index=False)

print("\nCompleted Successfully!")