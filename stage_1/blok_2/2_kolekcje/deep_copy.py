# co jeśli mamy listę w liście i ją skopiujemy
# copy() , list() oraz [:] są kopiami płytkimi
# zakupy
import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_styczen = [nabial, chemia]
print("Zakupy w styczniu: ")
print(zakupy_styczen)

"""
sprawdźmy rózne metody kopiowania kolekcji
"""
# zakupy_luty = zakupy_styczen
# zakupy_luty = copy.copy(zakupy_styczen)
# zakupy_luty = zakupy_styczen[:]
zakupy_luty = copy.deepcopy(zakupy_styczen)
print("Zakupy w lutym (kopia) ze stycznia: ")
print(zakupy_luty)

zakupy_styczen.append("gabka")
print("Zakupy w styczniu po dodaniu produktu: ")
print(zakupy_styczen)
print("Zakupy w lutym: ")
print(zakupy_luty)

# modyfikacja referencji
zakupy_styczen[0][0] = "keczup"
print("Zakupy w styczniu po dodaniu produktu: ")
print(zakupy_styczen)
print("Zakupy w lutym: ")
print(zakupy_luty)