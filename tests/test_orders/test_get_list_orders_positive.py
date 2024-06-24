import json


import requests
from unittest.mock import Mock
from unittest.mock import patch
from conftest import *
from data import *
from main.courier.create_new_courier import register_new_courier_and_return_login_password
from main.courier.helpers_courier import HelpersCourier
from main.orders.helpers_orders import HelpersOrders


class TestGetListOrdersPositive:

    def test_create_order_with_courier_id(self, courier):
        payload = {'courierId': courier}
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        assert response.status_code == 200

    def test_create_order_with_courier_id_and_nearest_station(self, courier):
        payload = {'courierId': courier, 'nearestStation': HelpersOrders.generate_nearest_station()}
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        assert response.status_code == 200

    def test_create_order_with_limit_and_page(self):
        payload = HelpersOrders.generate_parameters_with_limit_and_page()
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        assert response.status_code == 200

    def test_create_order_with_limit_and_page_and_nearest_station(self):
        payload = HelpersOrders.generate_parameters_with_limit_and_page_and_nearest_station()
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        assert response.status_code == 200
