import json

import pytest
import requests

from conftest import *
from data import *
from main.courier.helpers_courier import HelpersCourier


class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_create_order(self, color):
        order = HelpersCourier.generate_order()
        order["color"] = color
        response = requests.post(BASE_URL + ORDERS_PATH, data=json.dumps(order))

        assert response.status_code == 201 and 'track' in response.json()
