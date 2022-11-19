#słowniki
slownik = {"kwiatek": "storczyk",
           "doniczka": "duża",
           "ziemia": "1kg",
           "wartosc": 35.50}


print(slownik)

klucz_dodajemy = 1
wartosc_dodajemy = "jeden"
#dodanie elementu do słownika
print("dodajemy element do słownika:")
slownik[klucz_dodajemy] = wartosc_dodajemy
print(slownik)

# klucz_usuwamy
# element_usuwany = "kwiatek"
print("Usuwamy wpis - klucz - wartosc za pomoca usunięcia klucza:")
slownik.pop("kwiatek")
print(slownik)


# wartosc_zamieniamy
print("Zmieniamy wartosc slownika pod danym kluczem:")
wartosc_zmieniamy = "dwa"
slownik[1] = wartosc_zmieniamy
print(slownik)

#sprawdzamy czy klucz istnieje
# klucz_sprawdzamy = "blabla"
klucz_sprawdzamy = "ziemia"
if klucz_sprawdzamy in slownik.keys():
    print("drukujemy klucz")
    print(klucz_sprawdzamy)
    print("drukujemy wartosc")
    print(slownik[klucz_sprawdzamy])
else:
    print("Brak takiego klucza")

print("#"*120)
for key, value in slownik.items():
   print(key, value)
