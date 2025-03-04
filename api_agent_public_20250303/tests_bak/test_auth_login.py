import pytest
import requests

BASE_URL = "http://localhost:8001"

@pytest.mark.parametrize("test_id, payload, expected_status", [
    ("TC004", {"username": "testuser", "password": "testpass"}, 200),
    ("TC005", {"username": "wronguser", "password": "testpass"}, 401),
    ("TC006", {"username": "testuser", "password": "wrongpass"}, 401)
])
def test_user_login(api_client, test_id, payload, expected_status):
    response = api_client.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == expected_status
    if expected_status == 200:
        assert "access_token" in response.json()