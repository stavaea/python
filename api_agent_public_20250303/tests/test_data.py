VALID_REGISTER_DATA = {
    "username": "newuser",
    "password": "newpass123",
    "email": "new@example.com",
    "phone": "1234567890"
}

INVALID_REGISTER_DATA = {
    "username": "",
    "password": "short",
    "email": "invalid",
    "phone": "123"
}

VALID_LOGIN_DATA = {
    "username": "testuser",
    "password": "testpass"
}

INVALID_LOGIN_DATA = {
    "username": "wrong",
    "password": "credentials"
}

VALID_CART_ITEM = {
    "product_id": 1,
    "quantity": 2
}

INVALID_CART_ITEM = {
    "product_id": 999,
    "quantity": 1
}

VALID_ORDER_DATA = {
    "address_id": 1
}

INVALID_ORDER_DATA = {
    "address_id": 999
}