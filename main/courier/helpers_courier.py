import random
import string


class HelpersCourier:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_credentials(login=False, password=False, first_name=False):
        credentials = {}

        if login:
            credentials['login'] = HelpersCourier.generate_random_string(10)

        if password:
            credentials['password'] = HelpersCourier.generate_random_string(10)

        if first_name:
            credentials['first_name'] = HelpersCourier.generate_random_string(10)

        return credentials

    @staticmethod
    def generate_credentials_with_another_password(credentials):
        password = HelpersCourier.generate_random_string(10)
        credentials_with_another_password = {'login': credentials['login'], 'password': password}

        return credentials_with_another_password
