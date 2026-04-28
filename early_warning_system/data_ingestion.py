import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def simulate_signals(region, days=365):
    """
    Simulates real-time signals for a given region.
    Signals include: food_price_index, news_sentiment, troop_movements.
    """
    date_today = datetime.now()
    dates = [date_today - timedelta(days=x) for x in range(days)]
    dates.reverse()

    seeds = {"Sudan": 42, "Libya": 43, "Rwanda": 44, "Syria": 45, "Yemen": 46, "Ukraine": 47, "Gaza": 48}
    np.random.seed(seeds.get(region, 50))

    food_prices = 100 + np.cumsum(np.random.normal(0.1, 2, days))
    news_sentiment = np.random.uniform(-1, 0.5, days)
    troop_movements = np.random.poisson(lam=5, size=days)

    df = pd.DataFrame({
        'ds': dates,
        'food_price_index': food_prices,
        'news_sentiment': news_sentiment,
        'troop_movements': troop_movements
    })

    return df

if __name__ == "__main__":
    for region in ["Sudan", "Libya", "Rwanda", "Syria", "Yemen", "Ukraine", "Gaza"]:
        data = simulate_signals(region)
        print(f"Simulated data for {region}:")
        print(data.head())
        data.to_csv(f"early_warning_system/data_{region.lower()}.csv", index=False)
