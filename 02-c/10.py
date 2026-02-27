# 02-c/10.py

def read_vector(text):
    print(text)
    x = float(input("What is value of x? "))
    y = float(input("What is value of y? "))
    return x, y

def dot_product(ax, ay, bx, by):
    return ax * bx + ay * by

ax, ay = read_vector("For vector A")
bx, by = read_vector("For vector B")

product = dot_product(ax, ay, bx, by)

print(f"Dot product of [{ax:.2f}, {ay:.2f}] and [{bx:.2f}, {by:.2f}] is {product:.2f}")
