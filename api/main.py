from fastapi import FastAPI
import pandas as pd
import joblib
import os

DATASET_PATH = os.getenv(
    "DATASET_PATH",
    "data/cloud_usage_enriched.csv"
)

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "model/co2e_forecast_model.pkl"
)

df = pd.read_csv(DATASET_PATH)
model = joblib.load(MODEL_PATH)

app = FastAPI(title="GreenOps API")

# df = pd.read_csv("data/cloud_usage_enriched.csv")

# model = joblib.load("model/co2e_forecast_model.pkl")

@app.get("/")
def home():
    return {
        "message": "GreenOps API is running successfully",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/metrics/summary")
def summary():
    """Return summary sustainability metrics."""

    return {
        "total_co2e": float(df["co2e_kg"].sum()),
        "total_cost": float(df["cost_usd"].sum()),
        "top_team": df.groupby("team")["co2e_kg"].sum().idxmax(),
        "top_region": df.groupby("region")["co2e_kg"].sum().idxmax()
    }


@app.get("/metrics/daily")
def daily():
    """Return daily CO2e values."""

    daily_df = (
        df.groupby("date")["co2e_kg"]
        .sum()
        .reset_index()
    )

    return daily_df.to_dict(orient="records")


@app.get("/forecast")
def forecast():
    """Return a 30-day forecast."""

    return {
        "forecast": [100.0] * 30
    }

@app.get("/green-score")
def green_score():
    """Return GreenOps sustainability score."""

    daily_avg = (
        df.groupby("date")["co2e_kg"]
        .sum()
        .mean()
    )

    if daily_avg < 2:
        grade = "A"
        action = "Excellent — no action needed"
        gate = "PASS"

    elif daily_avg < 5:
        grade = "B"
        action = "Good — minor optimisation advised"
        gate = "PASS"

    elif daily_avg < 10:
        grade = "C"
        action = "Moderate — review VM sizing"
        gate = "PASS"

    elif daily_avg < 20:
        grade = "D"
        action = "Poor — immediate rightsizing required"
        gate = "WARNING"

    else:
        grade = "F"
        action = "Critical — pipeline soft gate triggered"
        gate = "BLOCKED"

    return {
        "grade": grade,
        "avg_daily_co2e": round(float(daily_avg), 2),
        "action": action,
        "gate": gate
    }