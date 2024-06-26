import allure

from conftest import *

from main.courier.requests_courier import RequestsCourier


class TestLoginCourierPositive:
    @allure.title('Авторизация курьера с валидными логином и паролем')
    def test_login_courier_with_valid_credentials(self, create_courier):
        response = RequestsCourier.login_courier(create_courier)

        assert response.status_code == 200 and 'id' in response.json()
