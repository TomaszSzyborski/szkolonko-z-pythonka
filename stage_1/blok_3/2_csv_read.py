baza_osob = []

with open('osoby', 'r') as plik:
    # pierwsza linijka jest opisem kolumn dlatego wczytujemy ja
    # do oddzielnej listy
    opisy_kolumn = plik.readline()

    # odczytujemy dalsze linijki az do konca
    for line in plik:

        # usuwamy znaki niedrukowalne (whitespace) z linijki
        line = line.strip()

        # dzielimy linijke na elementy listy wedlug przecinkow
        osoba = line.split(',')

        # zmieniamy wiek na int
        osoba[2] = int(osoba[2])

        print(osoba)

        # dodajemy liste z danymi osoby do bazy
        baza_osob.append(osoba)


print()
print(baza_osob)
