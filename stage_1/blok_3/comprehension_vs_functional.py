sentence = 'I enjoy coding in Python!'
vowels = [i for i in sentence.lower() if i in 'aeiou']

consonants = [i for i in sentence.lower() if i.isalpha() if i not in vowels]

print(consonants)

print(list(filter(lambda letter: letter not in vowels, sentence)))
print(list(map(lambda letter: "_" if letter in vowels else letter, sentence)))


def get_price(price):
    return price if price > 0 else 0


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
real_prices = [p if p > 0 else 0 for p in original_prices]
real_prices_v2 = [get_price(p) for p in original_prices]
real_prices_v3 = list(map(get_price, original_prices))
real_prices_v4 = list(map(lambda p: p if p > 0 else 0, original_prices))

print(real_prices)
print(real_prices_v2)
print(real_prices_v3)
print(real_prices_v4)
