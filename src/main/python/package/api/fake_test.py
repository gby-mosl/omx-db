import random
from random import randint

from faker import Faker

from package.api.company import Company
from package.api.person import Person, Staff

fake = Faker(locale="fr_FR")

if __name__ == '__main__':

    # for _ in range(1, 20):
    #     company = Company(f"{fake.company()}", f"{fake.street_name()}", f"{fake.postcode()}", f"{fake.city()}")
    #     company.save()
    #
    # for _ in range(500):
    #     person = Person(f"{fake.last_name()}", f"{fake.first_name()}", f"{random.randint(2,20)}")
    #     person.save()

    # for _ in range(20):
    #     staff = Staff(f"{fake.last_name()}", f"{fake.first_name()}", f"{fake.job()}")
    #     staff.save()
    for _ in range(10):
        print(f"{fake.last_name()} {fake.first_name()}\n{fake.address()}\n{fake.job()}\n{fake.license_plate()}\n{'-'*50}")


