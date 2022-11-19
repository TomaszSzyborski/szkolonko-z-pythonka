from datetime import datetime
from pprint import pprint

from utils.fake_factory import fake


def get_comment():
    return {
        "text": fake.text(),
        "id": fake.random_int()
    }


def get_comment_with_author():
    return {
        "text": fake.text(),
        "id": fake.random_int(),
        "author": fake.name(),
    }


def get_comment_with_lots_of_other_data():
    return {
        "text": fake.text(),
        "id": fake.random_int(),
        "author": fake.name(),
        "ssn": fake.ssn(),
        "address": fake.address(),
    }

def get_comment_with_lots_of_other_data_and_date():
    return {
        "text": fake.text(),
        "id": fake.random_int(),
        "author": fake.name(),
        "ssn": fake.ssn(),
        "address": fake.address(),
        "createdAt": datetime.now(),
    }

if __name__ == '__main__':
    pprint(get_comment())
