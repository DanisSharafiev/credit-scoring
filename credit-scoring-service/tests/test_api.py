import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_credit_score():
    payload = {
        "interest_rate": 15.0,
        "outstanding_debt": 2000.0
    }
    response = client.post("/api/credit-score", json=payload)
    assert response.status_code == 200
    assert response.json()["credit_score"] in ["Good", "Bad"]