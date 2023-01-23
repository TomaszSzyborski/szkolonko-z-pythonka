from abc import ABC


class Item(ABC):
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price


# class Color(ABC):
#     def __init__(self, color):
#         self.color = color
#
#
# class Hair(Color):
#     def __init__(self, color, length):
#         super().__init__(color)
#         self.length = length


class Product(Item):
    def __init__(self, name: str, quantity: float, price: float):
        super().__init__(quantity, price)
        self.name = name


class Stock(Item):
    def __init__(self, product_name, quantity, price):
        super().__init__(quantity, price)
        self.product_name = product_name


def calculate_total(items: list[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Product('B', 5, 250)
])

print(total)

# calculate total an inventory list
total = calculate_total([
    Stock('Tablet', 5, 950),
    Stock('Laptop', 10, 850)
])

print(total)
