from conftest import *


class TestLoginCourierPositive:

    def test_login_courier_with_valid_credentials(self):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)

        assert response.status_code == 200 and 'id' in response.json()

        Helpers.delete_courier(payload)