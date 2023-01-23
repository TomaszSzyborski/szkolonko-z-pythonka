# ta zmienna imie jest w zakresie globalnym
from typing import Final

_IMIE: Final[str] = "ola"

# argument domyslny jest typem wartosciowym
def duza_litera(imie="ala"):
    global _IMIE
    # ta zmienna imie jest tylko w zakresie funkcji
    imie = imie.capitalize()
    # _IMIE = _IMIE.capitalize()
    return _IMIE

print("Argument domyślny:")
print(duza_litera())

print("Argument podany:")
print(duza_litera("tomasz"))


print("Zmienna globalna:")
print(_IMIE)

