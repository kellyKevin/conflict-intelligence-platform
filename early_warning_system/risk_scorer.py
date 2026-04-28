import pandas as pd
from prophet import Prophet
import os

def calculate_risk(region):
    csv_path = f"early_warning_system/data_{region.lower()}.csv"
    if not os.path.exists(csv_path):
        from data_ingestion import simulate_signals
        df = simulate_signals(region)
        df.to_csv(csv_path, index=False)
    else:
        df = pd.read_csv(csv_path)

    # Prepare data for Prophet
    # We'll use food_price_index as a proxy for 'y' (conflict risk indicator)
    prophet_df = df[['ds', 'food_price_index']].rename(columns={'food_price_index': 'y'})

    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Risk score normalized 0-100 based on forecast and trend
    latest_yhat = forecast['yhat'].iloc[-1]
    risk_score = min(max(latest_yhat / 3, 0), 100)

    return {
        "region": region,
        "current_risk_score": round(risk_score, 2),
        "trend": "increasing" if forecast['trend'].iloc[-1] > forecast['trend'].iloc[-30] else "decreasing"
    }

if __name__ == "__main__":
    for region in ["Sudan", "Libya", "Rwanda", "Syria", "Yemen", "Ukraine", "Gaza"]:
        risk = calculate_risk(region)
        print(risk)
