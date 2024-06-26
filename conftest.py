import pytest

from main.courier.requests_courier import RequestsCourier
from main.orders.helpers_orders import HelpersOrders
from main.orders.requests_orders import RequestsOrders


@pytest.fixture(scope='class')
def create_courier():
    credentials = RequestsCourier.create_courier_and_get_credential()

    yield credentials

    RequestsCourier.delete_courier(credentials)


@pytest.fixture(scope='class')
def courier_with_order():
    credentials = RequestsCourier.create_courier_and_get_credential()
    courier_login_response = RequestsCourier.login_courier(credentials)
    courier_id = courier_login_response.json()['id']

    order_creation_response = RequestsOrders.create_order(HelpersOrders.generate_order())
    order = RequestsOrders.get_order(HelpersOrders.generate_parameters_with_track_id(order_creation_response.json()['track']))
    RequestsOrders.accept_order(order.json()['order']['id'], courier_id)

    yield courier_id

    RequestsCourier.delete_courier(credentials)
