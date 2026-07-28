# Name: Tammineni Nagarjuna
# Lab 02 - Task 2

import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is NOT a Python keyword.")
    """
    Output:
    Enter a word: if
if is a Python keyword.
    """