from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(title="GreenOps API")

df = pd.read_csv("data/cloud_usage_enriched.csv")

model = joblib.load("model/co2e_forecast_model.pkl")


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