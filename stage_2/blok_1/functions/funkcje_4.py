# ta funkcja oddaje obliczona wartosc za pomoca slowa return
def kwadrat(liczba):
    wynik = liczba**2
    print(wynik)
    return wynik

# aby skorzystac ze zwracanej wartosci
# trzeba ja przypisac do zmiennej
wynik = kwadrat(2)

print("Wynik:", wynik)


