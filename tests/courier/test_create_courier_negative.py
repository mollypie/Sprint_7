from conftest import *


class TestCreateCourierNegative:

    def test_create_two_identical_couriers(self):
        payload = Helpers.generate_courier(login=True, password=True)
        courier_1 = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)
        courier_2 = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert courier_1.status_code == 201 and courier_2.status_code == 409

        Helpers.delete_courier(payload)

    def test_create_courier_without_password(self):
        payload = Helpers.generate_courier(login=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE

    def test_create_courier_without_login(self):
        payload = Helpers.generate_courier(password=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE
