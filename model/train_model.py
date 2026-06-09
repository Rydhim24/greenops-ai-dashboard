import pandas as pd

# Load data
df = pd.read_csv("data/cloud_usage_enriched.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Aggregate daily CO2e
daily = df.groupby("date")["co2e_kg"].sum().reset_index()

# Create features
daily["lag_7"] = daily["co2e_kg"].shift(7)
daily["lag_14"] = daily["co2e_kg"].shift(14)
daily["rolling_7"] = daily["co2e_kg"].rolling(7).mean()
daily["dow"] = daily["date"].dt.dayofweek

# Drop NaN rows
daily = daily.dropna()

print(daily.head())
print(daily.shape)

from sklearn.linear_model import LinearRegression

# Features and target
X = daily[["lag_7", "lag_14", "rolling_7", "dow"]]
y = daily["co2e_kg"]

# Last 30 days = test
X_train = X[:-30]
X_test = X[-30:]

y_train = y[:-30]
y_test = y[-30:]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")

from sklearn.metrics import mean_squared_error
import numpy as np

# Predictions
preds = model.predict(X_test)

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, preds))

print("RMSE:", rmse)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(
    y_test.values,
    label="Actual"
)

plt.plot(
    preds,
    label="Predicted"
)

plt.title("30-Day CO2e Forecast")
plt.xlabel("Days")
plt.ylabel("CO2e (kg)")
plt.legend()

plt.savefig("model/forecast_plot.png")

print("Forecast plot saved!")

import joblib

joblib.dump(model, "model/co2e_forecast_model.pkl")

print("Model saved!")