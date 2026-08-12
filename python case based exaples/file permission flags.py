read = 4
write = 2
execute = 1

permissions = read | write

write_permission = permissions & write

print("Permission value:", permissions)
print("Write permission set:", write_permission != 0)

# Output:
# Permission value: 6
# Write permission set: True