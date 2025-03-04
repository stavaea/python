import pytest
import requests

BASE_URL = "http://localhost:8001"

@pytest.mark.parametrize("test_id, payload, expected_status", [
    ("TC001", {"username": "newuser", "password": "newpass", "email": "newuser@example.com", "phone": "1234567890"}, 201),
    ("TC002", {"username": "", "password": "newpass", "email": "newuser@example.com", "phone": "1234567890"}, 422),
    ("TC003", {"username": "newuser", "password": "", "email": "newuser@example.com", "phone": "1234567890"}, 422)
])
def test_user_registration(api_client, test_id, payload, expected_status):
    response = api_client.post(f"{BASE_URL}/auth/register", json=payload)
    assert response.status_code == expected_status