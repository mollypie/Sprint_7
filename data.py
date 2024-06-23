
BASE_URL = 'https://qa-scooter.praktikum-services.ru'
LOGIN_COURIER_PATH = '/api/v1/courier/login'
CREATE_COURIER_PATH = '/api/v1/courier'
DELETE_COURIER_PATH = '/api/v1/courier/'

TEXT_SUCCESS_TRUE = '{"ok":true}'
TEXT_INSUFFICIENT_DATA_FOR_CREATE = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
TEXT_LOGIN_ALREADY_EXISTS = "Этот логин уже используется"
TEXT_REQUIRED_DATA_LOGIN = "Недостаточно данных для входа"
TEXT_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
TEXT_COURIER_NOT_FOUND = "Курьер с идентификатором {} не найден"  #.format(courierId)
