# wow w koncu bedziemy miec pomoc do funkcji!
# doc string zaczynamy i konczymy trzema apostrofami lub
# cudzyslowami

def kwadrat(liczba):
    ''' Zwraca kwadrat podanej liczby'''
    return liczba**2

def pole_prostokat(a, b):
    """
    Oblicza i zwraca pole prostokata

    (float, float) -> float
    :param a: bok a
    :param b: bok b
    :return: Pole prostokata
    """
    return a*b


if __name__ == '__main__':
    print(help(kwadrat))
    print(help(pole_prostokat))

    print(kwadrat(2))
    print(pole_prostokat(2, 4))
