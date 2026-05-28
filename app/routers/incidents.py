from fastapi import APIRouter
from typing import List
from app.models.schemas import Incident

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get(
    "",
    response_model=List[Incident],
    summary="Get all incidents"
)
def get_incidents():
    return [
        {
            "incident_id": 101,
            "charger_id": 2,
            "severity": "high",
            "description": "Charger overheating detected"
        },
        {
            "incident_id": 102,
            "charger_id": 1,
            "severity": "medium",
            "description": "Telemetry instability detected"
        }
    ]