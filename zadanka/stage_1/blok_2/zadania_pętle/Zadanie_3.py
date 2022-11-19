"""
Wymagania:
Napisz program wypisujący tabliczkę mnozenia (1 do 10)
dla podanej przez użytkownika liczby

Wynik powinien wyglądać tak:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
itd.
"""
liczba = int(input("Wprowadz liczbe: "))

i = 1
for i in range(1,11):
    wynik = liczba * i
    i+1
    print(f"{liczba} x {i} = {wynik}")
