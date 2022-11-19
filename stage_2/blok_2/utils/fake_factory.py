from faker import Faker
from faker.providers import internet, address, bank, ssn, job, profile, color

fake = Faker()

for provider in [internet, address, bank, ssn, job, profile, color]:
    fake.add_provider(provider)
