from conftest import create_courier

from conftest import *
from data import *
from main.courier.helpers_courier import HelpersCourier
from main.courier.requests_courier import RequestsCourier


class TestLoginCourierNegative:
    @pytest.mark.parametrize(
        'password',
        [
            None,
            ''
        ]
    )
    def test_login_courier_with_invalid_password(self, create_courier, password):
        response = RequestsCourier.login_courier({'login': create_courier['login'], 'password': password})

        assert response.status_code == 400 and response.text == TEXT_REQUIRED_DATA_LOGIN

    @pytest.mark.parametrize(
        'login',
        [
            None,
            ''
        ]
    )
    def test_login_courier_with_invalid_login(self, create_courier, login):
        response = RequestsCourier.login_courier({'login': login, 'password': create_courier['password']})

        assert response.status_code == 400 and response.text == TEXT_REQUIRED_DATA_LOGIN

    @pytest.mark.parametrize(
        'password',
        [
            HelpersCourier.generate_random_string(8),
            ' ',

        ]
    )
    def test_login_courier_with_non_existent_password(self, create_courier, password):
        response = RequestsCourier.login_courier({'login': create_courier['login'], 'password': password})

        assert response.status_code == 404 and response.text == TEXT_ACCOUNT_NOT_FOUND

    @pytest.mark.parametrize(
        'login',
        [
            HelpersCourier.generate_random_string(8),
            ' ',

        ]
    )
    def test_login_courier_with_non_existent_login(self, create_courier, login):
        response = RequestsCourier.login_courier({'login': login, 'password': create_courier['password']})

        assert response.status_code == 404 and response.text == TEXT_ACCOUNT_NOT_FOUND
