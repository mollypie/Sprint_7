from conftest import *
import requests

from data import *


class RequestsOrders:
    @staticmethod
    def get_orders(payload):
        response = requests.get(BASE_URL + ORDERS_PATH, params=payload)

        return response

    @staticmethod
    def create_order(payload):
        response = requests.post(BASE_URL + ORDERS_PATH, data=payload)

        return response

    @staticmethod
    def accept_order(order_id, courier_id):
        response = requests.put(BASE_URL + ACCEPT_ORDERS_PATH + str(order_id),
                                params=HelpersOrders.generate_parameters_with_courier_id(courier_id))

        return response

    @staticmethod
    def get_order(payload):
        response = requests.get(BASE_URL + GET_ORDER, params=payload)

        return response
