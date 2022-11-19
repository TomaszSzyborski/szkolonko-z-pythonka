import requests as r

pokemon_name = "pikachu"
url = "https://pokeapi.co/api/v2/"
response = r.get(f"{url}/pokemon/{pokemon_name}")
print(response)
# print(response.text)
print(response.headers)
print(response.json())

print("we want clearer things...")
my_json_dict = response.json()
