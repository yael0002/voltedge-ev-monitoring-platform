from fastapi import APIRouter
from app.models.schemas import Telemetry
from app.services.predictive_service import calculate_risk_score

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)


@router.post(
    "",
    summary="Submit telemetry data and calculate risk"
)
def submit_telemetry(data: Telemetry):
    has_error = data.temperature > 80 or data.power_kw > 170
    prediction = calculate_risk_score(
        temperature=data.temperature,
        power_kw=data.power_kw,
        has_error=has_error
    )

    return {
        "message": "Telemetry received",
        "charger_id": data.charger_id,
        "telemetry": data,
        "prediction": prediction
    }