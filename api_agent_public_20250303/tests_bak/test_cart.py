import pytest
import requests

BASE_URL = "http://localhost:8001"

def test_get_cart(api_client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = api_client.get(f"{BASE_URL}/cart", headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize("test_id, payload, expected_status", [
    ("TC011", {"product_id": 1, "quantity": 1}, 200),
    ("TC012", {"product_id": 999, "quantity": 1}, 422),
    ("TC013", {"product_id": 1, "quantity": 0}, 422)
])
def test_add_to_cart(api_client, auth_token, test_id, payload, expected_status):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = api_client.post(f"{BASE_URL}/cart/add", json=payload, headers=headers)
    assert response.status_code == expected_status