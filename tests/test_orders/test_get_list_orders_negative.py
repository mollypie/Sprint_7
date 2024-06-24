import json

import pytest
import requests
from unittest.mock import Mock
from unittest.mock import patch
from conftest import *
from data import *
from main.courier.create_new_courier import register_new_courier_and_return_login_password
from main.courier.helpers_courier import HelpersCourier


class TestGetListOrdersNegative:

    @patch('main.courier.helpers_courier.HelpersCourier.login_courier', return_value='123456')
    def test_create_order_with_courier_id(self, mock_courier_id):
        creds = register_new_courier_and_return_login_password()
        courier = HelpersCourier()
        courier_id = courier.login_courier(creds)
        payload = {'courierId': courier_id}
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        assert response.status_code == 404
