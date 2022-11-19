"""
Wymagania:
Napisz program obliczający liczbę liter i cyfr w podanym stringu
"""
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

podany_string = input("Wpisz dowolny string: ")

liczba_cyfr = 0
liczba_liter = 0

for i in podany_string:
    if i in cyfry:
        liczba_cyfr =1
    else:
        liczba_liter=+1

    print(f"Liczba cyfr: {liczba_cyfr} Liczba liter: {liczba_liter}")