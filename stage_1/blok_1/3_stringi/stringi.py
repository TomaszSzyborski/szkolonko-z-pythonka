"""
sprawdzenie typu wprowadzonego stringa
"""
print("A".isalnum())
print("2".isalnum())
print("$".isalnum())

print("a".isalpha())
print("2".isalpha())
print("$".isalpha())

print("a".isdigit())
print("2".isdigit())
print("$".isdigit())

"""
Program obliczający rok urodzenia po podaniu wieku
"""
wiek = input("Podaj wiek: ")

# wszystko co uzytkownik poda jest stringiem, nawet liczby
print(type(wiek))

# musimy zamienic str na int aby moc wykonac arytmetyke
rok_urodzenia = 2022 - int(wiek)
print(type(rok_urodzenia))
print(f"Twoj rok urodzenia to {rok_urodzenia}")

wzrost = input("podaj wzrost: ")

# formatowanie wartosci liczbowych
print(f"Twoj wzrost w centymetrach to {float(wzrost):.2f}")

print(f"Twoj wzrost w centymetrach to {wzrost}, a wiek w latach to {wiek}")

