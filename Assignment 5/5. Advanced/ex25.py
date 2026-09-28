s = input("Enter a string: ")
sub = input("Enter substring: ")

find_index = -1
count = 0

for i in range(len(s) - len(sub) + 1):
    match = True

    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break

    if match:
        if find_index == -1:
            find_index = i
        count += 1

print("First index:", find_index)
print("Count:", count)


# Output:
# Enter a string: banana
# Enter substring: ana
# First index: 1
# Count: 1