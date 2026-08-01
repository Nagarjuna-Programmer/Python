# Name: Tammineni Nagarjuna
# Lab 05 - Task 3

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

# Method 1: Comma-separated print()
print("Name:", name, "Marks:", marks)

# Method 2: str.format()
print("Name: {} Marks: {}".format(name, marks))

# Method 3: f-string
print(f"Name: {name} Marks: {marks}")
"""
Output:
Enter your name: T.Nagarjuna
Enter your marks: 545
Name: T.Nagarjuna Marks: 545
Name: T.Nagarjuna Marks: 545
Name: T.Nagarjuna Marks: 545
"""