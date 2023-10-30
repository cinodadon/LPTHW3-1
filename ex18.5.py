# This script defines four functions that print different messages.

# This one is a function with *args
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# This one is a function with explicit arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This one is a function with a single argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one is a function with no arguments
def print_none():
    print("I got nothin'.")

# Testing the functions
print_two("Sterling", "Redman")
print_two_again("Sterling", "Redman")
print_one("First!")
print_none()

