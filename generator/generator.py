from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        city=faker_ru.city(),
        country=faker_ru.country(),
        phone=faker_ru.msisdn(),
        address=faker_ru.address()
    )
        