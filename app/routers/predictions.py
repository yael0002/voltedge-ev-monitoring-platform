from fastapi import APIRouter
from typing import List
from app.models.schemas import Prediction

router = APIRouter(
    prefix="/predictions",
    tags=["Predictive Analytics"]
)


@router.get(
    "",
    response_model=List[Prediction],
    summary="Get prediction risk scores"
)
def get_predictions():
    return [
        {
            "charger_id": 1,
            "prediction_score": 0.22,
            "risk_level": "low"
        },
        {
            "charger_id": 2,
            "prediction_score": 0.87,
            "risk_level": "high"
        }
    ]