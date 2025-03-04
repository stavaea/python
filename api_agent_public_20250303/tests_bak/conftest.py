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
    # 假设我们有一个默认用户用于测试
    login_payload = {
        "username": "testuser",
        "password": "testpass"
    }
    response = api_client.post(f"{BASE_URL}/auth/login", json=login_payload)
    assert response.status_code == 200
    return response.json().get("access_token")