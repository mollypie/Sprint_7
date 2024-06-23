import json

import pytest
import requests

from conftest import *
from data import *
from main.courier.create_new_courier import register_new_courier_and_return_login_password
from main.courier.helpers import Helpers


class TestLoginCourierNegative:
    @pytest.mark.parametrize(
        "password",
        [
            None,
            ""
        ]
    )
    def test_login_courier_with_invalid_password(self, password):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={"login": payload["login"], "password": password})

        assert response.status_code == 400 and response.text == TEXT_REQUIRED_DATA_LOGIN

        Helpers.delete_courier(payload)

    @pytest.mark.parametrize(
        "login",
        [
            None,
            ""
        ]
    )
    def test_login_courier_with_invalid_login(self, login):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={"login": login, "password": payload["password"]})

        assert response.status_code == 400 and response.text == TEXT_REQUIRED_DATA_LOGIN

        Helpers.delete_courier(payload)

    @pytest.mark.parametrize(
        "password",
        [
            "vbvb1",
            " ",

        ]
    )
    def test_login_courier_with_non_existent_password(self, password):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={"login": payload["login"], "password": password})

        assert response.status_code == 404 and response.text == TEXT_ACCOUNT_NOT_FOUND

        Helpers.delete_courier(payload)

    @pytest.mark.parametrize(
        "login",
        [
            "vbvb1",
            " ",

        ]
    )
    def test_login_courier_with_non_existent_login(self, login):
        payload = register_new_courier_and_return_login_password()
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={"login": login, "password": payload["password"]})

        assert response.status_code == 404 and response.text == TEXT_ACCOUNT_NOT_FOUND

        Helpers.delete_courier(payload)
