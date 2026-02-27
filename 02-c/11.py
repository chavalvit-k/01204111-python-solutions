# 02-c/11.py

def read_one_input(text):
    value = float(input(f"Input length of {text}: "))
    return value

def read_multiple_inputs():
    a = read_one_input("side1")
    b = read_one_input("side2")
    c = read_one_input("side3")

    return a, b, c

def calculate_tri_perimeter(a, b, c):
    return a + b + c

def calculate_tri_area(p, a, b, c):
    s = p / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area

a, b, c = read_multiple_inputs()
p = calculate_tri_perimeter(a, b, c)
area = calculate_tri_area(p, a, b, c)

print(f"The perimeter of triangle is {p:.2f}")
print(f"The area of triangle is {area:.2f}")
