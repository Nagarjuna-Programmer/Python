percentage = 80
family_income = 150000

eligible = percentage > 85 or (percentage > 75 and family_income < 200000)

print("Eligible for scholarship:", eligible)

# Output:
# Eligible for scholarship: True