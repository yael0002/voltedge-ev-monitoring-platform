def calculate_risk_score(temperature: float, power_kw: float, has_error: bool = False):
    score = 0.0

    if temperature > 70:
        score += 0.4

    if power_kw > 150:
        score += 0.3

    if has_error:
        score += 0.3

    score = min(score, 1.0)

    if score >= 0.7:
        risk_level = "high"
    elif score >= 0.4:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "prediction_score": score,
        "risk_level": risk_level
    }
