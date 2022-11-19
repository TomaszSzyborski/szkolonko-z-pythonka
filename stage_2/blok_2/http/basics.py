import requests

from pprint import pprint
response = requests.get("https://lublin.eu/")
print(response.status_code)
pprint(response.headers)
print(response.content)
try:
    response.raise_for_status()
except Exception as e:
    print("Błąd: ", e)


response = requests.get("https://lublin.eu/turystyka/asdfasd")
print(response.status_code)
print(response.headers)
print(response.content)
try:
    response.raise_for_status()
except Exception as e:
    print("Błąd: ", e)


