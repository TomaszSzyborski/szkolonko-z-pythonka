name = "Janina"

samogloski = 0
spolgloski = 0

#enumerate zwraca tuple(?)
for index, litera in enumerate(name):
    print(index, litera)
    if litera in "aeuioy":
        samogloski += 1
    else:
        spolgloski += 1


print("Spolgloski:", spolgloski)
print("Samogloski:", samogloski)


