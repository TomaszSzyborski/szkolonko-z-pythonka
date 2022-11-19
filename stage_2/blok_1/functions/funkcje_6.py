# zmienna na poziomie globalnym
imie = "jola"

def drukuj_imiona(imie_2):
    # uzywamy slowa global i nazwe zmiennej globalnej
    # jesli chcemy ja uzyc wewnatrz funkcji - niepolecane!
    global imie
    imie = "ania"

    imie = str(imie).capitalize()
    imie_2 = str(imie_2).capitalize()

    print(imie, imie_2)

print("Zmienna globalna przed zmianą:")
print(imie)
# imiona takie same wypisano bo zmienna globalna
# zostala zmieniona wew. fukcji
drukuj_imiona("gosia")
print("Zmienna globalna po zmianie:")
print(imie)
