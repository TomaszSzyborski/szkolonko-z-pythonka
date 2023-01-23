# pola klasy

class Pracownik:
    '''Definiuje Pracownika'''

    # pola klasy - widoczne przez wszystkie instancje
    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, stanowisko):
        '''Konstruktor.
        imie, nazwisko - str, str
        '''
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = 0

        # aktualizujemy pole klasy liczba_pracownikow
        # przy tworzeniu kazdego nowego obiektu Pracownik
        Pracownik.liczba_pracownikow += 1

    def ustaw_wynagrodzenie(self, kwota):
        '''Ustawia wynagrodzenie Pracownika
        to jest metoda instancji - zmiany dokonuje w zmiennych instancji
        '''
        self.wynagrodzenie = kwota

    def daj_roczna_podwyzke(self):
        '''Daje roczna podwyzke - zwieksza wynagrodzenie o wartosc okresloną
        w polu klasy
        '''
        self.wynagrodzenie += self.wynagrodzenie * (1 / self.roczna_podwyzka)

        # gdyby implementacja obliczenia wygladala tak:
        # self.wynagrodzenie += self.wynagrodzenie * (karty / Pracownik.roczna_podwyzka)
        # to korzystalibyśmy zawsze z pola klasy roczna_podwyżka, nawet gdyby instancja
        # miała własną zmienną roczna_podwyzka

    def __str__(self):
        '''Własna implementacja dla wydruku obiektu'''
        return f'{self.imie} stanowisko: {self.stanowisko} pensja: {self.wynagrodzenie}'


    def __del__(self):
        '''Wlasna implementacja dla usuwania obiektu
        '''
        print('Pracownik {} zostal usunięty'.format(self.imie))
        Pracownik.liczba_pracownikow -= 1
        print('Aktualna liczba pracowników:'.format(Pracownik.liczba_pracownikow))




print('--- Tworzymy dwoch pracownikow i okreslamy wynagrodzenia ---')
prac1 = Pracownik('John Turturo', 'aktor')
prac2 = Pracownik('John Travolta', 'gwiazda')
print(prac1.wynagrodzenie)
prac1.typ_umowy = 'umowa o prace'
print(prac1.typ_umowy)
print(prac1.__dict__)
print(prac1)
# prac1.ustaw_wynagrodzenie(5000)
# prac2.ustaw_wynagrodzenie(8000)
# print(prac1)
# print(prac2)
#
# print('\n--- Sprawdzamy liczbe pracownikow - wyswietlamy pole klasy liczba_pracownikow ---')
# print('Pracownik.liczba_pracowników =', Pracownik.liczba_pracownikow)
# print('prac1.liczba_pracownikow =', prac1.liczba_pracownikow)
# print('prac2.liczba_pracownikow =', prac2.liczba_pracownikow)
#
# print('\n --- wysokość podwyżki ---')
# print('Pracownik.roczna_podwyzka =',Pracownik.roczna_podwyzka)
# print('prac1.roczna_podwyzka =',prac1.roczna_podwyzka)
# print('prac2.roczna_podwyzka', prac2.roczna_podwyzka)
#
# print('\n--- zmieniamy wys podwyzki na 8 ---')
# Pracownik.roczna_podwyzka = 8
# print('Pracownik.roczna_podwyzka =',Pracownik.roczna_podwyzka)
# print('prac1.roczna_podwyzka =',prac1.roczna_podwyzka)
# print('prac2.roczna_podwyzka', prac2.roczna_podwyzka)
#
# print('\n--- Patrzymy w namespace (__dict__) i widzimy do jakich atrybutow maja dostęp ---')
# print('\nPracownik.__dict__:\n',Pracownik.__dict__)
# print('\nprac1.__dict__:\n',prac1.__dict__)
# print('\nprac2.__dict__:\n',prac2.__dict__)
#
# print('\nJak widzimy instancje nie mają pola roczna_podwyzka, dlatego szukaja go wyzej w klasie')
#
# print('\n--- zmieniamy wys podwyzki w instancji prac2 na 12 ---')
# print('Jak widać wyżej, w __dict__ instancji prac2 nie ma pola roczna_podwyzka')
# prac2.roczna_podwyzka = 12
# print('Pracownik.roczna_podwyzka =',Pracownik.roczna_podwyzka)
# print('prac1.roczna_podwyzka =',prac1.roczna_podwyzka)
# print('prac2.roczna_podwyzka', prac2.roczna_podwyzka)
# print('\nWidzimy, ze wartosc zmienila sie tylko dla instancji prac2.')
# print("Zajrzyjmy jeszcze raz do namespace'ów:")
# print('\nPracownik.__dict__:\n',Pracownik.__dict__)
# print('\nprac1.__dict__:\n',prac1.__dict__)
# print('\nprac2.__dict__:\n',prac2.__dict__)
#
# print('Jak widzimy, teraz obiekt prac2 ma własną zmienną roczna_podwyzka, i z niej bedzie brac wartosc.')
# print('Obiekt prac1 nie ma takiej zmiennej, wiec dalej bedzie korzystac z wartosci w polu klasy\n')
#
# # del (prac2.roczna_podwyzka)
# print('--- Usuwamy pracownika prac2 ---')
# del prac2
# print(Pracownik.liczba_pracownikow)
#
# print('\n--- Teraz program się kończy i Python sam usuwa wszystkie pozostałe obiekty ---')
# print('--- Automatycznie wywoła destruktor __del__ dla pozostałych obiektów: ---\n')
