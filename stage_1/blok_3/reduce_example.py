from functools import reduce


def add(x, y):
    return x + y


my_list = [2, 4, 7, 3]
print(reduce(add, my_list))

my_list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, my_list))
initial_value = 10
print(f"With an {initial_value=}: " + str(reduce(lambda x, y: x + y, my_list, initial_value)))

list_of_strings = ["Blood", "for", "the", "Blood", "God"]

title_string = " WARHAMMER40k"
word_separator = "==="
to_be_printed = str(reduce(lambda word, next_word: f"{word}{word_separator}{next_word}"
                           , list_of_strings, title_string))
print(f"Reducing strings with {title_string=}: " + to_be_printed)
