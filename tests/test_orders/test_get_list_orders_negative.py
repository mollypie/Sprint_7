from unittest.mock import patch
from conftest import *
from data import *
from main.courier.requests_courier import RequestsCourier


class TestGetListOrdersNegative:

    @patch('main.courier.requests_courier.RequestsCourier.login_courier', return_value='123456')
    def test_get_order_with_non_exists_courier_id(self, mock_courier_id, create_courier):
        courier = RequestsCourier()

        courier_login_response = courier.login_courier(create_courier)
        parameters = HelpersOrders.generate_parameters_with_courier_id(courier_login_response)

        response = RequestsOrders.get_orders(parameters)

        assert response.status_code == 404 and response.text == TEXT_COURIER_NOT_FOUND
