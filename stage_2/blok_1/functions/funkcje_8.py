# argument domyslny jest typem referencyjnym
def dodaj_imie(imie, imiona=None):
    if imiona is None:
        imiona = []
    imiona.append(imie)
    return imiona

# jesli nie podamy argumentu domyslnego
# to Python utworzy typ referencyjny tylko przy pierwszym
# wywolaniu funkcji
# w tym przypadku jest to typ None
# i wewnątrz funkcji tworzymy nową listę jeśli jest nie podana wcześniej
print("Pierwsza lista:")
lista_imion = dodaj_imie("Ola")
print(lista_imion)
lista_imion = dodaj_imie("Ala", lista_imion)
print(lista_imion)
lista_imion = dodaj_imie("ela", lista_imion)
print(lista_imion)

# drugie wywolanie i dodajemy do nowej listy!
lista_imion2 = dodaj_imie("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie("Piotrek")
print(lista_imion3)
