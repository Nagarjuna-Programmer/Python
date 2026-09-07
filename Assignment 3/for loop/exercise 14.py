n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)

# Output:
# Enter a number: 22
# Factorial: 1124000727777607680000