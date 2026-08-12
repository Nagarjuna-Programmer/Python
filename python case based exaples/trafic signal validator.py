color = input("Enter traffic signal color: ").lower()

valid_colors = ["red", "yellow", "green"]

if color in valid_colors:
    print("Valid traffic light color")
else:
    print("Invalid traffic light color")

# Output:
# Enter traffic signal color: red
# Valid traffic light color