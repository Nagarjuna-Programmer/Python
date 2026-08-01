# Name: Tammineni Nagarjuna
# Lab 07 - Challenge

import argparse

parser = argparse.ArgumentParser(
    description="Add two numbers using named command-line arguments."
)

parser.add_argument("--num1", type=int, required=True,
                    help="First number")

parser.add_argument("--num2", type=int, required=True,
                    help="Second number")

args = parser.parse_args()

print("Sum =", args.num1 + args.num2)
"""
Output:
usage: lab07-challenge.py [-h] --num1 NUM1 --num2 NUM2
lab07-challenge.py: error: the following arguments are required: --num1, --num2
"""