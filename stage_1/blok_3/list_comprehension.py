# DEATH AND TAXES
net_price = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08


def get_price_with_tax(price: float):
    return price * (1 + TAX_RATE)


taxed = []
for price in net_price:
    final = price * (1 + TAX_RATE)
    taxed.append(final)
print(taxed)

taxed = []
for price in net_price:
    taxed.append(price * (1 + TAX_RATE))
print(taxed)

final_prices = [price * (1 + TAX_RATE) for price in net_price]
print(final_prices)

final_prices = [get_price_with_tax(price) for price in net_price]
print(final_prices)

# jak to działa?
# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable if conditional]

sentence = 'I enjoy coding in Python!'
vowels = [i for i in sentence.lower() if i in 'aeiou']

v = []
for i in sentence.lower():
    if i in 'aeiou':
        v.append(i)

vowels_slightly_more_readable = [letter for letter in sentence.lower() if letter in 'aeiou']
print(vowels)
print(vowels_slightly_more_readable)

# filtrowanie danych (można użyć labda i filter)
consonants1 = [i for i in sentence.lower() if i.isalpha() if i not in vowels]
consonants = [i for i in sentence.lower() if i.isalpha() and i not in vowels]
print(f"{consonants1=}")
print(f"{consonants=}")

# ale można też odwrócić szyk, żeby rezultat był inny - liczba rezultatów będzie taka sama jak w oryginalnym iterable


# warunek ? wartość_jeśli_warunek_True : wartość_jeśli_warunek_False
# wartość_jeśli_warunek_True if warunek else wartość_jeśli_warunek_False



new_list = [i if i.isalpha() else "_" for i in sentence.lower()]
print(f"{new_list=}")
print(f"{''.join(new_list)}")




def get_price(price):
    return price if price > 0 else 0


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
real_prices = [i if i > 0 else 0 for i in original_prices]
real_prices_v2 = [get_price(i) for i in original_prices]
print(real_prices)
print(real_prices_v2)
