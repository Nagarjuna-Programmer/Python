first_name = input("Enter first name: ")
roll_number = input("Enter roll number: ")

username = first_name.lower() + roll_number[-2:]

print("Username:", username)

# Output:
# Enter first name: nagarjuna
# Enter roll number: 25341a05k2
# Username: nagarjunak2