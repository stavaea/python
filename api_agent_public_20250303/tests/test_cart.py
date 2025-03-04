import allure
import pytest

@allure.feature("Cart Management")
class TestCartAPI:
    @allure.story("Get Cart")
    def test_get_cart(self, api_client, auth_token):
        with allure.step("Test Case TC007: Get cart with valid token"):
            headers = {"Authorization": f"Bearer {auth_token}"}
            response = api_client.get(f"{BASE_URL}/cart", headers=headers)
            assert response.status_code == 200

    @allure.story("Add to Cart")
    @pytest.mark.parametrize("test_id, payload, expected", [
        ("TC008", {"product_id": 1, "quantity": 2}, 200),
        ("TC009", {"product_id": 999, "quantity": 1}, 404)
    ])
    def test_add_to_cart(self, api_client, auth_token, test_id, payload, expected):
        with allure.step(f"Test Case {test_id}: Add item to cart"):
            headers = {"Authorization": f"Bearer {auth_token}"}
            response = api_client.post(
                f"{BASE_URL}/cart/add",
                json=payload,
                headers=headers
            )
            assert response.status_code == expected