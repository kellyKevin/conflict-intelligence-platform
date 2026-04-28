import pandas as pd
import numpy as np
from dowhy import CausalModel

class CounterfactualEngine:
    def __init__(self, data):
        self.data = data

    def run_simulation(self, treatment, outcome, common_causes):
        model = CausalModel(
            data=self.data,
            treatment=treatment,
            outcome=outcome,
            common_causes=common_causes
        )
        identified_estimand = model.identify_effect()
        estimate = model.estimate_effect(identified_estimand,
                                         method_name="backdoor.linear_regression")
        return estimate

def get_sample_data():
    # Simulated historical data
    # treatment: funding_amount, outcome: stability_index, common_cause: initial_poverty
    np.random.seed(42)
    num_samples = 1000
    initial_poverty = np.random.normal(50, 10, num_samples)
    funding_amount = 100 - initial_poverty + np.random.normal(0, 5, num_samples)
    stability_index = 0.5 * funding_amount - 0.2 * initial_poverty + np.random.normal(0, 10, num_samples)

    df = pd.DataFrame({
        'funding': funding_amount,
        'stability': stability_index,
        'poverty': initial_poverty
    })
    return df

if __name__ == "__main__":
    df = get_sample_data()
    engine = CounterfactualEngine(df)
    estimate = engine.run_simulation('funding', 'stability', ['poverty'])
    print(estimate)
