import json

import requests

from data import *
from main.courier.helpers_courier import HelpersCourier


def register_new_courier_and_return_login_password():
    payload = HelpersCourier.generate_courier(login=True, password=True)
    response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

    if response.status_code == 201:
        return payload

    return {}
