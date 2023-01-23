raw_slash = r"\ ".strip()
print(raw_slash)

my_string = r"something with slash \ inside"
print(raw_slash in my_string)
my_string = r"something with slash \inside"
print(raw_slash in my_string)

my_string = r"something with slash \ ".strip()
print(my_string.endswith(raw_slash))
