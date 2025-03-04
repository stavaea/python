import pytest
import requests
from typing import Dict, Any

BASE_URL = "http://localhost:8001"

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session

@pytest.fixture
def auth_token(api_client):
    login_payload = {
        "username": "testuser",
        "password": "testpass"
    }
    response = api_client.post(f"{BASE_URL}/auth/login", json=login_payload)
    return response.json().get("access_token")