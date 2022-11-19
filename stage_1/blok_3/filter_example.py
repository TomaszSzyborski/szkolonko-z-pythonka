# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(filter_object)  # generator
print(list(filter_object))  # lista

# With lambdas
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(filter_object)
print(list(filter_object))

print("what happens here?")
for value in list(filter_object):
    print(value)

for value in filter_object:
    print(value)

print(f"{filter_object=}")
print(f"{list(filter_object)=}")
