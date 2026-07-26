# Name: Tammineni Nagarjuna
# Lab 07 - Task 1

import sys

if len(sys.argv) != 2:
    print("Usage: python greet.py <name>")
else:
    print("Hello,", sys.argv[1] + "!")