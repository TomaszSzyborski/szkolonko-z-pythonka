# argument domyslny jest typem referencyjnym
def dodaj_imie_zle(imie, imiona=[]):
    imiona.append(imie)
    return imiona

# jesli nie podamy argumentu domyslnego
# to Python utworzy typ referencyjny tylko przy pierwszym
# wywolaniu funkcji
lista_imion = dodaj_imie_zle("Ola")
print(lista_imion)

# drugie wywolanie i myslimy ze dodajemy imie do nowej listy
# a okazuje sie ze to jest ta sama lista !
lista_imion2 = dodaj_imie_zle("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie_zle("Piotrek")
print(lista_imion3)
