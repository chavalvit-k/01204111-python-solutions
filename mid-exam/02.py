# mid_exam/02.py

def cal_room_volume(length, width, height):
    return length * width * height

def cal_cooling_power(volume):
    return volume * 850

length = float(input("Enter room length (m): "))
width = float(input("Enter room width (m): "))
height = float(input("Enter room height (m): "))

volume = cal_room_volume(length, width, height)
power = cal_cooling_power(volume)

print(f"Room Volume = {volume:.2f}")
print(f"Estimated Cooling Power = {power:.2f}")

if power <= 9000:
    print("Recommended AC Size: 9000 BTU/hr")
    print("Small")
elif power <= 12000:
    print("Recommended AC Size: 12000 BTU/hr")
    print("Medium")
elif power <= 18000:
    print("Recommended AC Size: 18000 BTU/hr")
    print("Large")
elif power <= 24000:
    print("Recommended AC Size: 24000 BTU/hr")
    print("Extra Large")
else:
    print("Please consult the engineer.")
