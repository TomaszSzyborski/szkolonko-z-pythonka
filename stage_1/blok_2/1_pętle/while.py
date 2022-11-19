
x = True

while x:
    print(x)
    x = False

# przyjmij hasło od uzytkownika
password = input("Podaj haslo: ")

# dopoki haslo nie spelni warunkow
while len(password) < 6:
    # napisz że hasło jest za krótkie
    if len(password) < 4:
        print("Bardzo slabe haslo")
    else:
        print("Slabe haslo")
    # przyjmi znowu haslo
    password = input("Podaj haslo, min. 6 znakow!: ")

# podziekuj za podanie prawidlowego hasla
print("Prawidlowe haslo")

