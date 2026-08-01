# Name: Tammineni Nagarjuna
# Lab 01 - Task 2

identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]

for name in identifiers:
    if name == "2value":
        print(name, "-> Invalid (starts with a digit)")
    elif name == "value_2":
        print(name, "-> Valid")
    elif name == "_hidden":
        print(name, "-> Valid")
    elif name == "class":
        print(name, "-> Invalid (Python keyword)")
    elif name == "my-var":
        print(name, "-> Invalid (contains '-')")
    elif name == "MyClass":
        print(name, "-> Valid")
    elif name == "total$":
        print(name, "-> Invalid (contains '$')")
'''
 ourput:
2value -> Invalid (starts with a digit)
value_2 -> Valid
_hidden -> Valid
class -> Invalid (Python keyword)
my-var -> Invalid (contains '-')
MyClass -> Valid
total$ -> Invalid (contains '$')'''