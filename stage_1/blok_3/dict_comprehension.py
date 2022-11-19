# dictionary comprehension example
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num * num
print(square_dict)

# dictionary = {key: value for vars in iterable}
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
prices1 = dict()
for product, price in old_price.items():
    prices1[product] = price * dollar_to_pound

new_price = {item: value*dollar_to_pound for item, value in old_price.items()}
print(new_price)


original_dict = {'jack': 38, 'michael': 48, 'guido': 57,
                 'john': 33, 'anna': 32, 'kirsten': 16,
                 'adam': 18, 'alexa': 32}

print(f"{original_dict=}")
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(f"{even_dict=}")

middle_aged_odd = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40 if v > 30}
print(f"{middle_aged_odd=}")

youngsters_even = {k: v for (k, v) in original_dict.items() if v % 2 == 0 if v < 20}
print(f"{youngsters_even=}")

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(f"{new_dict_1=}")