"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""
list = []
while True:
    try:
        data = input("Podaj dane numeryczne: ")
        if data == "N":
            break
        int_data = int(data)
        list.append(int_data)
        print(list)

    except ValueError:
        print("Podaj poprawne dane!")

