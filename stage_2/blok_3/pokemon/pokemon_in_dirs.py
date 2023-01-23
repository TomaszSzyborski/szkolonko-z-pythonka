import requests as r
import json
import os


pokemon_name = "pikachu"
url = "https://pokeapi.co/api/v2/"
response = r.get(f"{url}/pokemon/{pokemon_name}")

print("we want clearer things...")
my_json_dict = response.json()
for key, value in my_json_dict.items():
    print(f"{key=}")


print(json.dumps(response.json(), indent=4))

print(my_json_dict["sprites"]["back_default"])
for name, link in my_json_dict["sprites"].items():
    print(f"{name=} : {link=}")

card_types = ["front_shiny",  "front_shiny_female", "back_shiny"]
for card_type in card_types:
    with open(f"{pokemon_name}_{card_type}.png", "wb") as file:
        response = r.get(my_json_dict["sprites"][card_type])
        file.write(response.content)