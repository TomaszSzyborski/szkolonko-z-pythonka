# importujemy nasz kod, ktory sami napisalismy!


# import globalny
# import funkcje_9

# import relatywny - szczególna funkcja
from funkcje_9 import pole_prostokat

bok_a = float(input("Podaj bok <a> prostokąta: "))
bok_b = float(input("Podaj bok <b> prostokąta: "))

print("Pole prostokąta wynosi:")
print(pole_prostokat(bok_a, bok_b))
