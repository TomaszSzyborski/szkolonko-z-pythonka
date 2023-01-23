krystyna = {"kwiatek": "Selenicereus grandiflorus",
           "doniczka": "bardzo duża",
           "ziemia": "5kg",
           "wartosc": 250,
           "ozdoby": "oplot z rzemini"}

agnieszka = {"kwiatek": "hiacynt",
             "liczba kwiatów": 5,
             "doniczka": "duża",
             "ziemia": "1kg",
             "wartosc": 250}

# wyrzuci błąd
# print(prezent["ozdoby"])

print(krystyna["kwiatek"])
print(agnieszka["kwiatek"])
# print(agnieszka["ozdoby"])
print(krystyna.get("ozdoby", "wstążka"))
print(agnieszka.get("ozdoby", "wstążka"))
print(agnieszka.get("ozdoby"))

print(krystyna.items())
for key, value in krystyna.items():
    print(f"{key} = {value}")

krystyna.update(agnieszka)
print(krystyna)
agnieszka.update(krystyna)
print(agnieszka)
krystyna.update({"kokardka": "turkusowa"})
print(krystyna)
krystyna["kokardka"] = "amarant"
print(krystyna)
krystyna["odżywka"] = "do sukulentów"
print(krystyna)
del krystyna["odżywka"]
print(krystyna)

for kursantka in [krystyna, agnieszka]:
    print(kursantka["kwiatek"])
    print(kursantka["doniczka"])
    kursantka["wartosc"] += 50
    print(kursantka)