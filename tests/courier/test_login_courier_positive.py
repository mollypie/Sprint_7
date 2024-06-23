import json

import requests

from conftest import *
from data import *
from main.courier.create_new_courier import register_new_courier_and_return_login_password
from main.courier.helpers import Helpers


class TestLoginCourierPositive:

    def test_login_courier_with_valid_credentials(self):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=payload)

        assert response.status_code == 200 and 'id' in response.json()

        Helpers.delete_courier(payload)
