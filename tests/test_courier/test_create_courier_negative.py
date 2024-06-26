from data import *
from main.courier.helpers_courier import HelpersCourier
from main.courier.requests_courier import RequestsCourier


class TestCreateCourierNegative:

    def test_create_two_identical_couriers(self):
        credentials = HelpersCourier.generate_credentials(login=True, password=True)
        courier_1 = RequestsCourier.create_courier(credentials)
        courier_2 = RequestsCourier.create_courier(credentials)

        assert courier_1.status_code == 201 and courier_2.status_code == 409

        RequestsCourier.delete_courier(credentials)

    def test_create_with_exists_login(self):
        credentials = HelpersCourier.generate_credentials(login=True, password=True)
        new_credentials = HelpersCourier.generate_credentials_with_another_password(credentials)

        RequestsCourier.create_courier(credentials)
        courier_2 = RequestsCourier.create_courier(new_credentials)

        assert courier_2.status_code == 409 and courier_2.text == TEXT_LOGIN_ALREADY_EXISTS

        RequestsCourier.delete_courier(credentials)

    def test_create_courier_without_password(self):
        credentials = HelpersCourier.generate_credentials(login=True)
        response = RequestsCourier.create_courier(credentials)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE

    def test_create_courier_without_login(self):
        credentials = HelpersCourier.generate_credentials(password=True)
        response = RequestsCourier.create_courier(credentials)

        assert response.status_code == 400 and response.text == TEXT_INSUFFICIENT_DATA_FOR_CREATE
