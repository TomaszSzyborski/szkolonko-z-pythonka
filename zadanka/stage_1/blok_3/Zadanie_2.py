"""
Wymagania:
Napisz program który stworzy plik csv (nazwij go dane_zadanie_2.csv) z danymi pobieranymi od użytkownika:
Imię, Nazwisko, Rok_Urodzenia. (w pętli)
Użyj funkcji
Użyj obsługi błędów aby upewnić się, że rok jest daną numeryczną
Dodaj kolumnę "Wiek", wartość ma być obliczona z obecnego roku przy użyciu danych z kolumny Rok_Urodzenia


Następnie otwórz plik i wypisz jego zawartość na ekran.
"""

while True:
    try:
        name = input("Podaj imię i nazwisko: ")
        year = input("Podaj date urodzenia: ")
        year_int = int(year)
        wiek = 2022 - year_int

        dane = {
            "imię i nazwisko": name,
            "data urodzenia": year,
            "wiek": wiek,
        }

        with open("dane_zadanie_2.csv" "a") as file:
            file.write(f"{dane}")

    except ValueError:
        print("Podaj poprawny rok!")

    except FileNotFoundError:
        with open("dane_zadanie_2.csv" "x") as file:
            file.write(f"{dane}")
