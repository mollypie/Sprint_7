import requests

from conftest import *
from data import *
from main.courier.helpers_courier import HelpersCourier


class TestCreateCourierNegative:

    def test_create_two_identical_couriers(self):
        payload = HelpersCourier.generate_courier(login=True, password=True)
        courier_1 = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)
        courier_2 = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert courier_1.status_code == 201 and courier_2.status_code == 409

        HelpersCourier.delete_courier(payload)

    def test_create_with_exists_login(self):
        new_password = "hghghgh"
        payload = HelpersCourier.generate_courier(login=True, password=True)
        requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data={"login": payload["login"], "password": new_password})

        assert (response.status_code == 409 and response.text == TEXT_LOGIN_ALREADY_EXISTS)

        HelpersCourier.delete_courier(payload)

    def test_create_courier_without_password(self):
        payload = HelpersCourier.generate_courier(login=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE

    def test_create_courier_without_login(self):
        payload = HelpersCourier.generate_courier(password=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE
