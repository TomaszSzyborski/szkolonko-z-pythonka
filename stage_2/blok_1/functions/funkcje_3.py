# mozemy miec kilka argumentow wymaganych oraz kilka domyslnych
# argumenty domyslne musza byc po wymaganych
def wypisz_dane(imie, nazwisko, kurs="Python", liczba_dni=15, *args, **kwargs):
    print(kwargs)
    for element in args:
        print(f"obsługuję: {element}")
    print(f"Imię: {imie}\n"
          f"Nazwisko: {nazwisko}\n"
          f"Kurs: {kurs}\n"
          f"Liczba dni: {liczba_dni}\n")

# argumenty wymagane (in. pozycyjne) musza byc podane
wypisz_dane("Tomasz", "Sz.")

# tutaj podajemy wszystkie wartosci argumentow
wypisz_dane("jan", "kowalski", "Java", 80,3,3,33,3,3,3,3,3,3,3,3,3,"asdfasd")

# kolejnosc argumentow mozna zmieniac, ale trzeba uzyc nazw zmiennych
wypisz_dane("gosia", "nowak", liczba_dni=30, kurs="JavaScript")
wypisz_dane(kurs="Java", imie="gosia", liczba_dni=23, nazwisko="nowak")

dane = {
    "imie": "Adam",
    "nazwisko": "Iewa",
    "kurs": "groovy",
    "liczba_dni": 71,
    "warzywko": "pomidor"
}
wypisz_dane(**dane)
