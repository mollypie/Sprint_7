import random
import string

import requests

from faker import Faker

from data import BASE_URL, LOGIN_COURIER_PATH, DELETE_COURIER_PATH


class HelpersOrders:
    @staticmethod
    def generate_parameters_for_get_orders():

        return

    @staticmethod
    def generate_nearest_station():
        metro_station = [str(random.randint(1, 224))]
        return metro_station

    @staticmethod
    def generate_parameters_with_limit_and_page():
        parameters = {'limit': str(random.randint(1, 30)), 'page': 0}

        return parameters

    @staticmethod
    def generate_parameters_with_limit_and_page_and_nearest_station():
        parameters = {'limit': str(random.randint(1, 30)),
                      'page': 0,
                      'nearestStation': HelpersOrders.generate_nearest_station()}

        return parameters
