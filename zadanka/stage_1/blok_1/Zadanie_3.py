"""
Wymagania:
Sprawdź czy podany rok jest rokiem przestępnym.
Rezultat wypisz na ekran.

Podpowiedź:
jest podzielny przez 4, ale nie jest podzielny przez 100
jest podzielny przez 400
"""

rok = int(input("Wpisz rok: "))

if rok % 4 == 0 and rok % 100 != 0:
    print("Rok przestępny")
elif rok % 400 == 0:
    print("Rok przestępny")
else:
    print("Rok nieprzestępny")


