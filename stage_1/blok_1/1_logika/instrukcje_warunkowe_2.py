"""
Program pytający użytkownika o imię.
Zakładamy, że jeśli imię kończy się na "a" to z dużą dozą prawdopodobieństwa graniczą
z pewnością jest to kobieta.

Tak, wiem - jest np. Azja Tuchajbejowicz.
"""

name = input("Podaj Imie: ")

if name.endswith("a") and not name == "Jan Maria":
    print(f"Dzień dobry Pani {name}.")
elif name == "Jan Maria":
    print("Uszanowanie, Panie Rokita.")
    print(">>Ni to baba ni to chłop a diabeł w nim chodzi<<")
else:
    print(f"Czołem Panie {name}!")


