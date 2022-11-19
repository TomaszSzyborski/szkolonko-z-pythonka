my_first_list = [1, 2, 3, 4]
my_second_List = ["apple", "banana", "orange", "pear"]
zipped = zip(my_first_list, my_second_List)
print(zipped)
print(*zipped)


# magic: zip to dict
magic_snort_snort = dict(zipped)
print(magic_snort_snort)
# but why empty?
zipped = zip(my_first_list, my_second_List)
magic_snort_snort = dict(zipped)
print(magic_snort_snort)
print(zipped)
print("myzip before")
print(*zipped)
print("myzip after")
lista_zipped = list(zip(my_first_list, my_second_List))
for _ in range(5):
    print(lista_zipped)