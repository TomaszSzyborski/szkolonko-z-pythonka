# usuwanie elementow z listy
lista = ["kwiatek", "doniczka", "ziemia", "woda"]
x = lista.pop(-2)
print(x)
print(lista)
lista.remove("doniczka")
print(lista)
# lista.remove("doniczka")
# print(lista)

element_usuwany = "doniczka"

if element_usuwany in lista:
    lista.remove(element_usuwany)
else:
    print("Niema takiego elementu")

print(lista)

