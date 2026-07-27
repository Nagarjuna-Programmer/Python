# Name: Tammineni Nagarjuna
# Lab 01 - Challenge

import keyword

def is_valid_identifier(name):

    if len(name) == 0:
        return False

    if keyword.iskeyword(name):
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False

    for ch in name:
        if not (ch.isalnum() or ch == "_"):
            return False

    return True


test_names = [
    "value",
    "_hidden",
    "2value",
    "class",
    "my_var",
    "my-var"
]

for item in test_names:
    print(item, ":", is_valid_identifier(item))