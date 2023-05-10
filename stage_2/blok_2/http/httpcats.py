import requests as r

animal = "cat"
if animal == "cat":
    url = "https://http.cat"
else:
    url = "https://http.dog"

resp = r.get(f"{url}/200.jpg")
print(resp.headers)
print(resp.content)


with open(f"{animal}.jpg", "wb") as file:
    file.write(resp.content)
