import random
import string

import requests

from data import BASE_URL, LOGIN_COURIER_PATH, DELETE_COURIER_PATH


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def delete_courier(payload):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)
        courier_id = response.json()
        response_delete = requests.delete(BASE_URL + DELETE_COURIER_PATH + str(courier_id['id']))
        assert response_delete.status_code == 200

    @staticmethod
    def generate_courier(login=False, password=False, first_name=False):
        credentials = {}

        if login:
            credentials['login'] = Helpers.generate_random_string(10)

        if password:
            credentials['password'] = Helpers.generate_random_string(10)

        if first_name:
            credentials['first_name'] = Helpers.generate_random_string(10)

        return credentials
