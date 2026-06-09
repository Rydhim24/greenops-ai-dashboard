import streamlit as st
import requests
import pandas as pd

st.title("🌱 GreenOps Dashboard")

# Summary Metrics
summary = requests.get(
    "http://127.0.0.1:8000/metrics/summary"
).json()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total CO2e (kg)",
    round(summary["total_co2e"], 2)
)

col2.metric(
    "Total Cost (USD)",
    round(summary["total_cost"], 2)
)

col3.metric(
    "Highest Emission Team",
    summary["top_team"]
)

# Daily Trend
st.subheader("Daily CO2e Trend")

daily = requests.get(
    "http://127.0.0.1:8000/metrics/daily"
).json()

daily_df = pd.DataFrame(daily)

st.line_chart(
    daily_df.set_index("date")["co2e_kg"]
)

# Forecast
if st.button("Show Forecast"):

    forecast = requests.get(
        "http://127.0.0.1:8000/forecast"
    ).json()

    st.subheader("30-Day Forecast")

    st.line_chart(
        forecast["forecast"]
    )