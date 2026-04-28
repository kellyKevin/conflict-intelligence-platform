def calculate_ethical_risk(autonomy_level, target_confidence, civilian_density, proportionality):
    """
    Calculates an ethical risk score (0-100).
    - autonomy_level: 0 (manual) to 1 (full)
    - target_confidence: 0 to 1
    - civilian_density: 0 (empty) to 1 (crowded)
    - proportionality: 0 (low) to 1 (high impact)
    """

    # Risk increases with autonomy, density, and impact, and decreases with confidence.
    base_risk = (autonomy_level * 30) + (civilian_density * 40) + (proportionality * 30)
    confidence_mitigation = target_confidence * 20

    risk_score = base_risk - confidence_mitigation
    return round(min(max(risk_score, 0), 100), 2)

if __name__ == "__main__":
    # Test case: Sudan 2026 scenario
    score = calculate_ethical_risk(0.8, 0.85, 0.9, 0.7)
    print(f"Ethical Risk Score for Sudan 2026: {score}")
