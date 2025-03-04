import allure
import pytest

@allure.feature("Authentication")
class TestAuthRegister:
    @allure.story("User Registration")
    @pytest.mark.parametrize("test_id, payload, expected", [
        ("TC001", {
            "username": "newuser",
            "password": "newpass123",
            "email": "new@example.com",
            "phone": "1234567890"
        }, 201),
        ("TC002", {
            "username": "",
            "password": "short",
            "email": "invalid",
            "phone": "123"
        }, 422)
    ])
    def test_user_registration(self, api_client, test_id, payload, expected):
        with allure.step(f"Test Case {test_id}: Register user"):
            response = api_client.post(f"{BASE_URL}/auth/register", json=payload)
            assert response.status_code == expected