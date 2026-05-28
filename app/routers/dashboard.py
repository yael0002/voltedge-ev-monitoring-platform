from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard KPIs"]
)


@router.get(
    "/kpis",
    summary="Get dashboard KPI metrics"
)
def get_dashboard_kpis():
    return {
        "active_chargers": 124,
        "incident_rate": 3.2,
        "average_session_duration": 41,
        "energy_consumption_kwh": 12450,
        "prediction_alerts": 7
    }