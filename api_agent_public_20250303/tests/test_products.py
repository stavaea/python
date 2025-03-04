import allure
import pytest

@allure.feature("Product Management")
class TestProductAPI:
    @allure.story("Get Products")
    @pytest.mark.parametrize("test_id, params, expected", [
        ("TC005", {"category_id": 1, "page": 1, "size": 10}, 200),
        ("TC006", {"category_id": None, "page": 2, "size": 5}, 200)
    ])
    def test_get_products(self, api_client, test_id, params, expected):
        with allure.step(f"Test Case {test_id}: Get products"):
            response = api_client.get(f"{BASE_URL}/products", params=params)
            assert response.status_code == expected
            if expected == 200:
                assert isinstance(response.json(), list)