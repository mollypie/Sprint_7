from conftest import *

from main.orders.helpers_orders import HelpersOrders
from main.orders.requests_orders import RequestsOrders


class TestGetListOrdersPositive:

    def test_get_list_orders_with_courier_id(self, courier_with_order):
        parameters = HelpersOrders.generate_parameters_with_courier_id(courier_with_order)
        response = RequestsOrders.get_orders(parameters)

        orders = response.json()['orders']

        assert (response.status_code == 200
                and all(courier_with_order == order.get("courierId") for order in orders))

    def test_get_list_orders_with_limit_and_page(self):
        parameters = HelpersOrders.generate_parameters_with_limit_and_page()
        response = RequestsOrders.get_orders(parameters)

        orders = response.json()['orders']

        assert (response.status_code == 200 and len(orders) == 10)
