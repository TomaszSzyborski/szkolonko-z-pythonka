"""
Jasio zbiera karty piłkarzy.
Każdą nową (unikalny numer identyfikacyjny) zapisuje na końcu pliku (wynikiem jest zawsze jednolinijkowy plik csv)

Napisz klasę Jasio, która będzie miała pole liczba_kart
oraz metody wczytujące i modyfikujące plik "karty_jasia.csv"

Napisz metodę wypisującą ile kart brakuje Jasiowi do zebrania pełnej kolekcji wiedząc,
że pełna kolekcja zawiera 18000 unikalnych kart
"""
"""
mając listę owoców
stwórz słowniki mające jako klucze nazwy rozpoczynające się wielką literą
1. jako warotści długości nazw
2. jako wartości ceny będące sumą kodów ASCII pierwszej i ostatniej litery podzieloną przez długość nazwy
"""

fruits = ['apple', 'mango', 'banana', 'cherry', 'passionfruit', 'dragonfruit', 'date']

for fruit in fruits:
    fruit.capitalize()