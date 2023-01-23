# ta funkcja oddaje obliczona wartosc za pomoca slowa return
def kwadrat(liczba):
    wynik = liczba**2
    print(wynik)
    return wynik

# aby skorzystac ze zwracanej wartosci
# trzeba ja przypisac do zmiennej
wynik = kwadrat(2)

print("Wynik:", wynik)

from typing import Final

_IMIE: Final[str] = "tomek"

# argument domyslny jest typem wartosciowym
def duza_litera(imie="tomek"):
    global _IMIE
    # ta zmienna imie jest tylko w zakresie funkcji
    imie = imie.capitalize()
    _IMIE = _IMIE.capitalize()
    return _IMIE
