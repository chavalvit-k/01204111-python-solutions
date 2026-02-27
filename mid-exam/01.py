# mid_exam/01.py

ADULT_COST = 100
CHILD_COST = 50

adults = int(input("How many adults?: "))
children = int(input("How many children?: "))
day = input("Which day?: ")

if day == "w":
    total_cost = adults * ADULT_COST * 0.7 + children * CHILD_COST
    discount_text = "(Wed discount)"
else:
    total_cost = adults * ADULT_COST + children * CHILD_COST
    discount_text = "(No discount)"

print(f"{discount_text} {adults} adults {children} children total {total_cost:.0f} Baht.")
