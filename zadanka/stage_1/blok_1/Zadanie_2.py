"""
Wymagania:
Napisz algorytm wystawiający ocenę na podstawie punktów uzyskanych na egzaminie
podaj ocenę na podstawie progu procentowego
5 od 90 do 100, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50
Rezultat wypisz na ekran.

Podpowiedź:
przyjmij dane od uzytkownika
zweryfikuj dane
wypisz odpowiedni wynik lub komentarz dotyczący wprowadzonych danych
"""

wynik_egzaminu = int(input("Wpisz wynik egzaminu: "))

if wynik_egzaminu > 89:
    print(" Ocena 5")
elif wynik_egzaminu > 79:
    print(" Ocena 4+")
elif wynik_egzaminu > 69:
    print(" Ocena 4")
elif wynik_egzaminu > 59:
    print(" Ocena3+")
elif wynik_egzaminu > 49:
    print(" Ocena 3")
else:
    print("Ocena 1")

