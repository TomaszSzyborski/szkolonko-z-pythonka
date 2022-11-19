import requests as r
from pprint import pprint
import json
pokemon_name = "pikachu"
url = "https://pokeapi.co/api/v2/"
response = r.get(f"{url}/pokemon/{pokemon_name}")
print(response)
print(response.headers)
print(response.json())

print("we want clearer things...")
my_json_dict = response.json()
pprint(my_json_dict)