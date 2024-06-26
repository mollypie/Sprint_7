import json

import pytest
import requests

from data import *
from main.orders.helpers_orders import HelpersOrders


class TestCreateOrder:

    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]
    )
    def test_create_order(self, color):
        order = HelpersOrders.generate_order()
        order['color'] = color
        response = requests.post(BASE_URL + ORDERS_PATH, data=json.dumps(order))

        assert response.status_code == 201 and 'track' in response.json()
