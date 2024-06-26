from data import *
from main.courier.helpers_courier import HelpersCourier
from main.courier.requests_courier import RequestsCourier


class TestCreateCourierPositive:

    def test_create_courier_with_first_name(self):
        credentials = HelpersCourier.generate_credentials(login=True, password=True, first_name=True)
        response = RequestsCourier.create_courier(credentials)

        assert response.status_code == 201 and response.text == TEXT_SUCCESS_TRUE

        RequestsCourier.delete_courier(credentials)

    def test_create_courier_without_first_name(self):
        credentials = HelpersCourier.generate_credentials(login=True, password=True)
        response = RequestsCourier.create_courier(credentials)

        assert response.status_code == 201 and response.text == TEXT_SUCCESS_TRUE

        RequestsCourier.delete_courier(credentials)
