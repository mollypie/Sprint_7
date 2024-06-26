import requests

from data import *
from main.courier.helpers_courier import HelpersCourier


class RequestsCourier:
    @staticmethod
    def create_courier_and_get_credential():
        payload = HelpersCourier.generate_credentials(login=True, password=True)

        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        if response.status_code == 201:
            return payload

        return {}

    @staticmethod
    def create_courier(payload):
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        return response

    @staticmethod
    def login_courier(payload):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)

        return response

    @staticmethod
    def delete_courier(payload):
        courier = RequestsCourier.login_courier(payload)

        response = requests.delete(BASE_URL + DELETE_COURIER_PATH + str(courier.json()['id']))

        return response
