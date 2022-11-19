"""
Wymagania:
Pobierz od użytkownika nazwę miesiąca.
Pobierz od użytkownika rok.

Wskaż liczbę dni w miesiącu.
Rezultat wypisz na ekran.
"""

miesiac = (input("Podaj miesiac: ")).lower()
rok = int(input("Podaj rok: "))

is_leap_year = rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0)

if miesiac == "luty" and is_leap_year:
    print(f"{miesiac} ma 29 dni")
elif miesiac == "luty":
    print(f"{miesiac} ma 28 dni")
elif miesiac == "kwiecien" or miesiac == "czerwiec" or miesiac == "pazdziernik" or miesiac == "listopad":
    print(f"{miesiac} ma 30 dni")
else:
    print(f"{miesiac} ma 31 dni")