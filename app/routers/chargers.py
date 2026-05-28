from fastapi import APIRouter
from typing import List
from app.models.schemas import Charger

router = APIRouter(
    prefix="/chargers",
    tags=["Chargers"]
)


@router.get(
    "",
    response_model=List[Charger],
    summary="Get all chargers"
)
def get_chargers():
    return [
        {
            "charger_id": 1,
            "location": "Copenhagen",
            "status": "online"
        },
        {
            "charger_id": 2,
            "location": "Aarhus",
            "status": "offline"
        }
    ]


@router.get(
    "/{charger_id}",
    response_model=Charger,
    summary="Get charger by ID"
)
def get_charger(charger_id: int):
    return {
        "charger_id": charger_id,
        "location": "Odense",
        "status": "online"
    }