# 04-b/01.py

def f(x):
    if x <= 15:
        return 2 * x + 10
    elif 15 < x <= 35:
        return 3 * x ** 2
    else:
        return 2 * x ** 3 - 5

def display_f(x, y):
    print(f"f({x:.3f}) = {y:.3f}")

x = float(input("Enter a real number: "))
y = f(x)
display_f(x, y)
