# ta zmienna imie jest w zakresie globalnym
imie = "ola"

# argument domyslny jest typem wartosciowym
def duza_litera(imie="ala"):
    # ta zmienna imie jest tylko w zakresie funkcji
    imie = imie.capitalize()
    return imie

print("Argument domyślny:")
print(duza_litera())

print("Argument podany:")
print(duza_litera("tomasz"))


print("Zmienna globalna:")
print(imie)

