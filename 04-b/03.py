# 04-b/03.py

import sys

def read_nonnegative(text):
    length = float(input(text))
    
    if length < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()
    else:
        return length

def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def is_right_triangle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return True
    else:
        return False

a = read_nonnegative("Enter 1st line's length: ")
b = read_nonnegative("Enter 2nd line's length: ")
c = read_nonnegative("Enter 3rd line's length: ")

if not is_triangle(a, b, c):
    print("It's not a triangle.")
elif is_triangle(a, b, c) and not is_right_triangle(a, b, c):
    print("It's a triangle but not a right triangle.")
else:
    print("It's a right triangle.")
