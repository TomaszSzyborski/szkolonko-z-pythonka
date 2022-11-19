# ta funkcja ma zdefiniowany jeden argument domyslny imie
# jesli uzytkowniknie poda wartosci to zostanie uzyta
# domyslna wartosc - "Franek"
def wypisz_imie(imie="franek"):
    imie = imie.capitalize()
    print(imie)

# uzytkownik nie musi podawac wartosci argumentu domyslnego
print("Imię domyślne: ")
wypisz_imie()

# albo moze podac swoja wartosc
print("Imię podane: ")
wypisz_imie("arek")
wypisz_imie("marta")
wypisz_imie("jola")
