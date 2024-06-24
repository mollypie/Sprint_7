import json
import random
import string

import requests

from faker import Faker

from data import BASE_URL, LOGIN_COURIER_PATH, DELETE_COURIER_PATH


class HelpersCourier:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_courier(payload):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)
        courier_id = response.json()
        return courier_id['id']

    @staticmethod
    def delete_courier(payload):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)
        courier_id = response.json()
        response_delete = requests.delete(BASE_URL + DELETE_COURIER_PATH + str(courier_id))
        assert response_delete.status_code == 200

    @staticmethod
    def delete_courier1(courier_id):
        response_delete = requests.delete(BASE_URL + DELETE_COURIER_PATH + str(courier_id))
        assert response_delete.status_code == 200

    @staticmethod
    def generate_courier(login=False, password=False, first_name=False):
        credentials = {}

        if login:
            credentials['login'] = HelpersCourier.generate_random_string(10)

        if password:
            credentials['password'] = HelpersCourier.generate_random_string(10)

        if first_name:
            credentials['first_name'] = HelpersCourier.generate_random_string(10)

        return credentials

    @staticmethod
    def generate_order():
        fake = Faker('ru_RU')
        address = random.choices(['Каляева, 13', 'Пушкина, 462', 'Мира, 174'])
        order = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": ''.join(address),
            "metroStation": random.randint(1, 224),
            "phone": fake.phone_number(),
            "rentTime": random.randint(1, 7),
            "deliveryDate": f'2024-{random.randint(1, 12)}-{random.randint(1, 28)}',
            "comment": HelpersCourier.generate_random_string(20)
        }

        return order
