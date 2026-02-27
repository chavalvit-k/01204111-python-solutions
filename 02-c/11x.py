# 02-c/_11x.py

import math

def read_multiple_inputs():
    a = read_one_input("side1")
    b = read_one_input("side2")
    c = read_one_input("side3")

    return a, b, c

def read_one_input(text):
    value = float(input(f"Input length of {text}: "))
    return value

def calculate_tri_perimeter(a, b, c):
    return a + b + c

def calculate_tri_area(s, a, b, c):
    s /= 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def display_all_outputs(shape, measure1, value1, measure2, value2):
    print(f"The {measure1} of {shape} is {value1:.2f}")
    print(f"The {measure2} of {shape} is {value2:.2f}")

a,b,c = read_multiple_inputs()
s = calculate_tri_perimeter(a,b,c)
area = calculate_tri_area(s,a,b,c)
display_all_outputs("triangle", "perimeter", s, "area", area)