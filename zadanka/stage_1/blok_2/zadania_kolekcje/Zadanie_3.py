"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""
slownik = {}
while True:
    klucz = input("Wpisz klucz: ")
    wartosc = input("Wpisz wartosc: ")
    czy_dalej = input("Czy chcesz podać kolejne? T lub N")


    if czy_dalej == "N":
        break

