# baza

osoba = ['pamela', 'anderson', 50]

# zmieniamy wszystkie dane w liście na string
# za pomoca list comprehension (czyli działania wew. listy)
# ale zachowujemy oryginalną liste, a tworzymy druga
osoba_str = [str(dane) for dane in osoba]

# laczymy dane z lity do jednego str za pomoca przecinków
dane_do_zapisu = ','.join(osoba_str)

# otwieram plik w trybie do dopisywania
with open('osoby.csv', 'a') as plik:
    plik.write(dane_do_zapisu + '\n')

