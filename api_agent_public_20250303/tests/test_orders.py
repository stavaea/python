import allure
import pytest

@allure.feature("Order Management")
class TestOrderAPI:
    @allure.story("Create Order")
    @pytest.mark.parametrize("test_id, payload, expected", [
        ("TC010", {"address_id": 1}, 200),
        ("TC011", {"address_id": 999}, 404)
    ])
    def test_create_order(self, api_client, auth_token, test_id, payload, expected):
        with allure.step(f"Test Case {test_id}: Create order"):
            headers = {"Authorization": f"Bearer {auth_token}"}
            response = api_client.post(
                f"{BASE_URL}/orders/create",
                json=payload,
                headers=headers
            )
            assert response.status_code == expected