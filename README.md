# VoltEdge EV Monitoring Platform

## Project Overview

VoltEdge EV Monitoring Platform is a Minimum Viable Product (MVP) developed to support intelligent monitoring of electric vehicle charging infrastructure.

The solution focuses on:

* Charger monitoring
* Telemetry data collection
* Incident management
* Predictive analytics
* KPI reporting and dashboard support

The project demonstrates how Business Architecture, Domain Driven Design (DDD), FastAPI and Business Intelligence can be combined to create a scalable monitoring platform.

---

## Technologies Used

* Python 3
* FastAPI
* Pydantic
* SQLite
* Docker
* GitHub
* Pytest

---

## Project Structure

app/

* main.py

Dockerfile

requirements.txt

README.md

---

## API Endpoints

### Chargers

* GET /chargers
* GET /chargers/{charger_id}

### Telemetry

* POST /telemetry

### Incidents

* GET /incidents

### Predictive Analytics

* GET /predictions

### Dashboard KPIs

* GET /dashboard/kpis

### System Health

* GET /
* GET /health

---

## Installation

Clone repository:

git clone https://github.com/yael0002/voltedge-ev-monitoring-platform.git

Navigate to project folder:

cd voltedge-ev-monitoring-platform

Install dependencies:

pip install -r requirements.txt

Run application:

uvicorn app.main:app --reload --port 8001

---

## API Documentation

After starting the application, Swagger documentation is available at:

http://127.0.0.1:8001/docs

---

## Testing

Run tests using:

pytest

---

## Author

Yassmin Salma El Kounti

EK – Økonomi og IT

Semester Project 2026
