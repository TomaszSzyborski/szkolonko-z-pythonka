# oblicz ilosc liczb parzystych i nieparzystych w zakresie
zakres = range(1, 101)
parzyste = 0
nieparzyste = 0

for liczba in zakres:

    licznik_for = 0

    # jesli parzysta to dodac do licznika parzystych
    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

    licznik_for += 1

print(f"Parzyste: {parzyste}, nieparzyste: {nieparzyste}")
print(licznik_for)





