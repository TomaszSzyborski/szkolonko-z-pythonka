class Eukarionty:
    domena = "Eukarionty"


class Zwierzeta(Eukarionty):
    krolestwo = "zwierzeta"


class Strunowce(Zwierzeta):
    typ = "strunowce"


class Kregowce(Strunowce):
    podtyp = "kregowce"


class Ssaki(Kregowce):
    gromada = "ssaki"


class Zyworodne(Ssaki):
    podgromada = "Żyworodne"


class Lozyskowce(Zyworodne):
    infragromada = "łożyskowce"


class Drapiezne(Lozyskowce):
    rzad = "Drapiezne"

    def poluj(self):
        print("Zaczajam się...")
        print("Skaczę!")
        print("Zagryzam")


class Kotowate(Drapiezne):
    rodzina = "kotowate"
    pazury_na_wierzchu = False

    def wysun_pazury(self):
        if self.pazury_na_wierzchu:
            print("No już bardziej wysunąć nie mogę...")
        else:
            self.pazury_na_wierzchu = True

    def schowaj_pazury(self):
        if self.pazury_na_wierzchu:
            self.pazury_na_wierzchu = False
        else:
            print("No już bardziej schować nie mogę...")


class Kot(Kotowate):
    rodzaj = "Kot"

    def daj_glos(self):
        print("miauuuu")


class KotDomowy(Kot):
    gatunek = "Kot domowy"

    def __init__(self, imie):
        self.imie = imie

    def mrucz(self):
        print("mrrrrr")


puszek = KotDomowy(imie="Puszek")
# do sprawdzenia hierarchii klas
import inspect

print(inspect.getmro(type(puszek)))
hierarchia = inspect.getmro(type(puszek))
for klasa in reversed(hierarchia[:-1]):
    nazwa_klasy = str(klasa).split(".")[-1][:-2]
    print(nazwa_klasy)

print(f"Czy puszek nalezy do klasy Eukarionty?: {isinstance(puszek, Eukarionty)}")
print(f"Czy puszek nalezy do klasy Zwierzeta?: {isinstance(puszek, Zwierzeta)}")
print(f"Czy puszek nalezy do klasy Strunowce?: {isinstance(puszek, Strunowce)}")
print(f"Czy puszek nalezy do klasy Kregowce?: {isinstance(puszek, Kregowce)}")
print(f"Czy puszek nalezy do klasy Ssaki?: {isinstance(puszek, Ssaki)}")
print(f"Czy puszek nalezy do klasy Zyworodne?: {isinstance(puszek, Zyworodne)}")
print(f"Czy puszek nalezy do klasy Lozyskowce?: {isinstance(puszek, Lozyskowce)}")
print(f"Czy puszek nalezy do klasy Drapiezne?: {isinstance(puszek, Drapiezne)}")
print(f"Czy puszek nalezy do klasy Kotowate?: {isinstance(puszek, Kotowate)}")
print(f"Czy puszek nalezy do klasy Kot?: {isinstance(puszek, Kot)}")
print(f"Czy puszek nalezy do klasy KotDomowy?: {isinstance(puszek, KotDomowy)}")

# jak puszek sie zachowa
print(f"Czy puszek ma pazury na wierzchu? {puszek.pazury_na_wierzchu}")
puszek.schowaj_pazury()
print(f"Czy puszek ma pazury na wierzchu? {puszek.pazury_na_wierzchu}")
puszek.wysun_pazury()
print(f"Czy puszek ma pazury na wierzchu? {puszek.pazury_na_wierzchu}")
puszek.wysun_pazury()
print(f"Czy puszek ma pazury na wierzchu? {puszek.pazury_na_wierzchu}")
puszek.schowaj_pazury()
print(f"Czy puszek ma pazury na wierzchu? {puszek.pazury_na_wierzchu}")

print("Jaki glos ma Puszek?")
puszek.daj_glos()
print("Drapie Puszka za uszkiem:")
puszek.mrucz()
print("Puszek widzi wrobla:")
puszek.poluj()

print("Sprawdzam czym jest puszek odwolujac sie do dziedziczonych zmiennych:")
print(puszek.domena)
print(puszek.krolestwo)
print(puszek.typ)
print(puszek.podtyp)
print(puszek.gromada)
print(puszek.podgromada)
print(puszek.infragromada)
print(puszek.rzad)
print(puszek.rodzina)
print(puszek.rodzaj)
print(puszek.gatunek)
