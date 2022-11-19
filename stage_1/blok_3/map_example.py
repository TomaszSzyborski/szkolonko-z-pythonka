# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)

print(map_object) # generator
print(list(map_object)) # lista

#With lambdas
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(map_object)
print(list(map_object))

print("what happens here?")
for value in list(map_object):
    print(value)

for value in map_object:
    print(value)

print(f"{map_object=}")
print(f"{list(map_object)=}")