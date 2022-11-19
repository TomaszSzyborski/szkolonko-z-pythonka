"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.
"""

liczba = int(input("Wpisz liczbę: "))

if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7 == 0:
    print("Jest podzielna")