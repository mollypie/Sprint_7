import pytest
import requests

from data import *
from main.courier.create_new_courier import register_new_courier_and_return_login_password
from main.courier.helpers_courier import HelpersCourier


@pytest.fixture(scope='class')
def courier():
    creds = register_new_courier_and_return_login_password()

    response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data=creds)
    response_data = response.json()
    courier_id = response_data['id']

    yield courier_id

    HelpersCourier.delete_courier1(courier_id)
