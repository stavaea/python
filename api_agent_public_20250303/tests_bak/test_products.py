import pytest
import requests

BASE_URL = "http://localhost:8001"

@pytest.mark.parametrize("test_id, params, expected_status", [
    ("TC007", {"category_id": 1, "page": 1, "size": 10}, 200),
    ("TC008", {"category_id": None, "page": 1, "size": 10}, 200),
    ("TC009", {"category_id": 999, "page": 1, "size": 10}, 200)
])
def test_get_products(api_client, test_id, params, expected_status):
    response = api_client.get(f"{BASE_URL}/products", params=params)
    assert response.status_code == expected_status