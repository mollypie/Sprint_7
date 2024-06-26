import random

from faker import Faker

from main.courier.helpers_courier import HelpersCourier


class HelpersOrders:
    @staticmethod
    def generate_parameters_with_courier_id(courier_id):
        parameters = {'courierId': courier_id}

        return parameters

    @staticmethod
    def generate_parameters_with_limit_and_page():
        parameters = {'limit': 10,
                      'page': 0}

        return parameters

    @staticmethod
    def generate_parameters_with_track_id(track_id):
        parameters = {'t': track_id}

        return parameters

    @staticmethod
    def generate_order():
        fake = Faker('ru_RU')
        address = random.choices(['Каляева, 13', 'Пушкина, 462', 'Мира, 174'])
        order = {
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'address': ''.join(address),
            'metroStation': random.randint(1, 224),
            'phone': fake.phone_number(),
            'rentTime': random.randint(1, 7),
            'deliveryDate': f'2024-{random.randint(1, 12)}-{random.randint(1, 28)}',
            'comment': HelpersCourier.generate_random_string(20)
        }

        return order
