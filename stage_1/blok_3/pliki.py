# Tworząc oprogramowanie często spotykamy się z sytuacją gdy chcemy uzyskać dostęp oraz zarządzać pewnymi zasobami.
# Takimi jak na przykład operacje na plikach czy połączenie do bazy danych.
# Zasoby te często posiadają pewne ograniczenia więc dobrą praktyką jest ich zwolnienie zaraz po zakończeniu ich używania.
# Python pozwala nam na łatwe zarządzanie tymi zasobami dostarczając nam pomoc, którą jest menadżer kontekstu.
# https://realpython.com/python-mmap/

# otwieranie pliku i wpisywanie tekstu

# otwarcie pliku
f = open("test.txt", 'w', encoding='utf-8')
try:
    # wpisanie tekstu do pliku test.txt
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
finally:
    # zamknięcie pliku niezależnie czy uda się coś wpisać do pliku
    f.close()

# Alternatywnie możemy użyć operatora `with` który zabezpieczy nam zamknięcie pliku(wywołanie __exit__)
# operator pozwalający otworzyć plik i go zamknąć(czyli wywołać funkcje __enter__ i __exit__)
# |    funkcja zwracająca context_menager z otwartym plikiem
# |    |       ścieżka do pliku
# |    |       |       opcje otwarcia pliku (r- read, w-write, a -append)
# |    |       |       |        codowanie
# |    |       |       |        |              operator przypisania obiektu zwróconego przez funkcje `open`
# |    |       |       |        |              |  jako zmienna `f`
# V    V       V       V        V              V  V
with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

# odczyt z pliku
with open("test.txt", 'r', encoding='utf-8') as f:
    print(f.readline())

# opcje odczytu pliku
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)


###############

dane = {
    "imie": "Andrzej",
    "nazwisko": "Klusiewicz",
    "adres": {
        "miasto": "Warszawa",
        "kod": "02-019"
    },
    "jezyki": ["polski", "angielski", "Java", "R", "Python", "PL/SQL"]
}

# możemy zapisywać słowniki do jsona
import json

with open('dane.json', mode='w', encoding='utf-8') as f:
    json.dump(dane, f)
