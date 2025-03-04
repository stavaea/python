import allure
import pytest

@allure.feature("Authentication")
class TestAuthLogin:
    @allure.story("User Login")
    @pytest.mark.parametrize("test_id, payload, expected", [
        ("TC003", {"username": "testuser", "password": "testpass"}, 200),
        ("TC004", {"username": "wrong", "password": "credentials"}, 401)
    ])
    def test_user_login(self, api_client, test_id, payload, expected):
        with allure.step(f"Test Case {test_id}: Login user"):
            response = api_client.post(f"{BASE_URL}/auth/login", json=payload)
            assert response.status_code == expected
            if expected == 200:
                assert "access_token" in response.json()