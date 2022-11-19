from abc import ABC
from typing import Protocol


class Item(ABC):
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price


class Product(Item):
    def __init__(self, name: str, quantity: float, price: float):
        super().__init__(quantity, price)
        self.name = name


def calculate_total(items: list[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Product('B', 5, 250)
])

print(total)


class Stock(Item):
    def __init__(self, product_name, quantity, price):
        super().__init__(quantity, price)
        self.product_name = product_name


# calculate total an inventory list
total = calculate_total([
    Stock('Tablet', 5, 950),
    Stock('Laptop', 10, 850)
])

print(total)
