from fastapi import FastAPI

from app.routers import chargers
from app.routers import telemetry
from app.routers import incidents
from app.routers import predictions
from app.routers import dashboard

app = FastAPI(
    title="VoltEdge EV Monitoring Platform API",
    description="""
    API platform for intelligent EV charger monitoring, telemetry ingestion,
    incident management, predictive analytics and dashboard KPI reporting.
    """,
    version="1.0.0"
)

app.include_router(chargers.router)
app.include_router(telemetry.router)
app.include_router(incidents.router)
app.include_router(predictions.router)
app.include_router(dashboard.router)


@app.get("/", tags=["System Health"], summary="Root endpoint")
def root():
    return {
        "message": "VoltEdge EV Monitoring Platform API is running"
    }


@app.get("/health", tags=["System Health"], summary="Check API health")
def health_check():
    return {
        "status": "healthy",
        "service": "VoltEdge EV Monitoring API"
    }