"""
Liczby całkowite, rzeczywiste i zespolone
oraz Decimal
"""
from decimal import Decimal

a = 3
b = 4

x = b / (2.0 + a)
print(x)

# najpierw wykona sie to co z prawej strony znaku =
# a dopiero potem nastapi przypisanie do zmiennej z lewej strony znaku =
w = 0.1 + 0.1 + 0.1 == 0.3

# hmmm przeciez powinno być True
print("Nasza zmienna W")
print(w)
print((0.1 + 0.1) == 0.2)
print(0.1 + 0.1 + 0.1)
print(0.3)
#
# # zwiekszamy precyzje i widzimy, ze ludzkie 0.3 nie ma odpowiednika
# # w komputerowym 0.3. Niektore warotsci komputer moze tylko podac
# # w przyblizeniu
print("{:.17f}".format(0.3))
print("{:.3f}".format(0.3))

#nowszy typ
print(f"{0.3:.17f}")
print(f"{0.3:.3f}")

z = round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10)
print(z)

x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(y)
print(z)

# zespolone
z = 1j
print(z)

z = -1j
print(z)

x = 3+5j
y = 5j
z = -5j

print(x)
print(y)
print(z)

print('Decimals')
one = Decimal('1')
three = Decimal('3')
big_d = Decimal(one/three)
print(big_d + big_d + big_d)
big_d = one/three
print(big_d + big_d + big_d)

x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')

print(x == Decimal('0.3'))
print(float(x) == 0.3)
print(x)