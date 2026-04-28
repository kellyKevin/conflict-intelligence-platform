import pandas as pd
import numpy as np
from engine import CounterfactualEngine

def scenario_marshall_plan():
    # If Marshall Plan had no money for Germany 1948, what's P(WW3 by 1960)?
    # Simulated data reflecting historical context
    np.random.seed(48)
    n = 500
    us_aid = np.random.choice([0, 1], size=n, p=[0.5, 0.5]) # 1 if aid provided
    economic_recovery = 0.7 * us_aid + np.random.normal(0, 0.1, n)
    prob_ww3 = 0.8 - 0.6 * economic_recovery + np.random.normal(0, 0.05, n)

    df = pd.DataFrame({'us_aid': us_aid, 'economic_recovery': economic_recovery, 'prob_ww3': prob_ww3})
    engine = CounterfactualEngine(df)
    estimate = engine.run_simulation('us_aid', 'prob_ww3', ['economic_recovery'])

    print("Scenario: Marshall Plan")
    print(f"Estimated Effect of Aid on P(WW3): {estimate.value:.4f}")

def scenario_cold_war():
    print("\nScenario: Cold War Escalation")
    # Simulation logic for Cold War...
    print("Estimated P(Escalation) under different communication protocols.")

def scenario_african_independence():
    print("\nScenario: African Independence Movements")
    # Simulation logic for African independence...
    print("Impact of colonial exit strategies on long-term stability.")

if __name__ == "__main__":
    scenario_marshall_plan()
    scenario_cold_war()
    scenario_african_independence()
