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
from zadanka.stage_1.blok_3.Zadanie_3 import calculate_bmi

koszykarz_bmi = calculate_bmi(180, 2.2)
print(f"{koszykarz_bmi=}")
