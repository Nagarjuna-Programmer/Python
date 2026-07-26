# Name: Tammineni Nagarjuna
# Lab 02 - Challenge

import keyword

print("Soft Keywords:")

if hasattr(keyword, "softkwlist"):
    for word in keyword.softkwlist:
        print(word)

print("\nHard Keywords:")

for word in keyword.kwlist:
    if not hasattr(keyword, "softkwlist") or word not in keyword.softkwlist:
        print(word)