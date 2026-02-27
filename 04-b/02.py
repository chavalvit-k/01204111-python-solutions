# 04-b/02.py

def read_point():
    print("Input a point (x,y):")
    x = float(input("x = ? "))
    y = float(input("y = ? "))

    return x, y

def location(x, y):
    if x == 0 and y == 0:
        return "at the origin"
    elif x == 0:
        return "on the y-axis"
    elif y == 0:
        return "on the x-axis"
    elif x > 0 and y > 0:
        return "in quadrant 1"
    elif x < 0 and y > 0:
        return "in quadrant 2"
    elif x < 0 and y < 0:
        return "in quadrant 3"
    elif x > 0 and y < 0:
        return "in quadrant 4"

def display_result(x, y, loc):
    print(f"The point ({x:.2f},{y:.2f}) is {loc}.")

x, y = read_point()
loc = location(x, y)
display_result(x, y, loc)
