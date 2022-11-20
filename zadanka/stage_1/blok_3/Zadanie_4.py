"""
Wymagania:
Utwórz plik dane_osobowe.csv z 10 wierszami, zawierającymi dane:
Imię, Nazwisko, Data_Urodzenia, Płeć, Adres_Ulica, Adres_Nr_Domu, Adres_Nr_Lokalu, Adres_Kod_Pocztowy, Adres_Miasto

Następnie na podstawie utworzonego pliku utwórz dwa nowe:
dane_kobiety.csv
dane_mezczyzni.csv
zawierające odpowiednie rekordy z pliku dane_osobowe.csv

Hint - możesz użyć biblioteki faker
"""

with open("dane_osobowe.csv", 'w') as file:
    file.write("Imię\n")
    file.write("Nazwisko\n")
    file.write("Data_Urodzenia\n")
    file.write("Płeć\n")
    file.write("Adres_Ulica\n")
    file.write("Adres_Nr_Domu\n")
    file.write("Adres_Nr_Lokalu\n")
    file.write("Adres_Kod_Pocztowy\n")
    file.write("Adres_Miasto\n")

with open("dane_kobiety.csv", 'w') as f:
