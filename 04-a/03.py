# 04-a/03.py

def compute_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def compute_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))

bmi = compute_bmi(weight, height)
status = compute_status(bmi)

print(f"BMI: {bmi:.2f}")
print(f"Weight status: {status}")
