# import pytest
# import requests
#
# from data import *
# from main.courier.create_new_courier import register_new_courier_and_return_login_password
# from main.courier.helpers import Helpers


# @pytest.fixture(scope='class')
# def courier():
#     login_pass = register_new_courier_and_return_login_password()
#     response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={'login: ' + login_pass[0], 'password: ' + login_pass[1]})


# @pytest.fixture(scope='function')
# def credentials():
#     return {
#         "login": Helpers.generate_random_string(10),
#         "password": Helpers.generate_random_string(10),
#         "first_name": Helpers.generate_random_string(10)
#     }
