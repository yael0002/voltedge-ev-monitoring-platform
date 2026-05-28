from pydantic import BaseModel


class Charger(BaseModel):
    charger_id: int
    location: str
    status: str


class Telemetry(BaseModel):
    charger_id: int
    voltage: float
    current: float
    power_kw: float
    temperature: float


class Incident(BaseModel):
    incident_id: int
    charger_id: int
    severity: str
    description: str


class Prediction(BaseModel):
    charger_id: int
    prediction_score: float
    risk_level: str
