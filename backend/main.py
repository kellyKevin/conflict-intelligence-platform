from fastapi import FastAPI, Query
import sys
import os

# Add component directories to path
sys.path.append(os.path.abspath("early_warning_system"))
sys.path.append(os.path.abspath("peace_treaty_analytics"))
sys.path.append(os.path.abspath("counterfactual_history"))
sys.path.append(os.path.abspath("ethics_frameworks"))

import risk_scorer
import analyzer
import engine
import risk_calculator

app = FastAPI(title="Conflict Intelligence & Ethics Platform API")

@app.get("/ews/risk-index")
def get_risk_index(region: str = "Sudan"):
    return risk_scorer.calculate_risk(region)

@app.get("/pta/treaty-analysis")
def get_treaty_analysis(text: str):
    ta = analyzer.TreatyAnalyzer()
    return ta.classify_clauses(text)

@app.get("/chm/counterfactual-query")
def get_counterfactual(treatment: str, outcome: str):
    # For now, return sample estimation based on our engine
    import pandas as pd
    import numpy as np
    np.random.seed(42)
    df = pd.DataFrame({
        treatment: np.random.normal(100, 10, 100),
        outcome: np.random.normal(50, 5, 100),
        'confounder': np.random.normal(0, 1, 100)
    })
    ce = engine.CounterfactualEngine(df)
    res = ce.run_simulation(treatment, outcome, ['confounder'])
    return {"treatment": treatment, "outcome": outcome, "effect": res.value}

@app.get("/efaw/ethical-score")
def get_ethical_score(autonomy: float, confidence: float, density: float, proportionality: float):
    score = risk_calculator.calculate_ethical_risk(autonomy, confidence, density, proportionality)
    return {"risk_score": score}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
