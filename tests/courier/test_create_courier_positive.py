from conftest import *


class TestCreateCourierPositive:

    def test_create_courier_with_first_name(self):
        payload = Helpers.generate_courier(login=True, password=True, first_name=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 201 and response.text == TEXT_SUCCESS_TRUE

        Helpers.delete_courier(payload)

    def test_create_courier_without_first_name(self):
        payload = Helpers.generate_courier(login=True, password=True)
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 201 and response.text == TEXT_SUCCESS_TRUE

        Helpers.delete_courier(payload)
