"""
Wymagania:
Stwórz listę kolorów.
Wypisz je w kolejności.

Następnie wybierz losowo jeden z kolorów,
przypisz go do nowej zmiennej i wypisz na ekran.

Podpowiedź:
Skorzystaj z modułu random
"""

import random

lista_kolorow = ["zielony", "zolty", "szary", "niebieski", "rozowy", "bialy"]

wybrany_kolor = random.choice(lista_kolorow)

print(wybrany_kolor)
