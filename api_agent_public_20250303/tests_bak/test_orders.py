import pytest
import requests

BASE_URL = "http://localhost:8001"

@pytest.mark.parametrize("test_id, payload, expected_status", [
    ("TC014", {"address_id": 1}, 200),
    ("TC015", {"address_id": 999}, 422),
    ("TC016", {"address_id": None}, 422)
])
def test_create_order(api_client, auth_token, test_id, payload, expected_status):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = api_client.post(f"{BASE_URL}/orders/create", json=payload, headers=headers)
    assert response.status_code == expected_status