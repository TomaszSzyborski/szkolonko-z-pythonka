lista = [[1, 2, [1,2,"marchewka"]], [4, 5, 6], [7, 8, 9]]

print(lista[0][2][2])

for element in lista:
    for subelement in element:
        print(subelement)
