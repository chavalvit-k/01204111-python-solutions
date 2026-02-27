# 02-c/09.py

TV_PRICE = 12000
AUDIO_PRICE = 6000

def read_amount():
    tv = int(input("How many TVs do you want? "))
    audio = int(input("How many audio systems do you want? "))
    return tv, audio

def compute_total(num_tv, num_audio):
    total = num_tv * TV_PRICE + num_audio * AUDIO_PRICE
    return total

num_tv, num_audio = read_amount()
total_amount = compute_total(num_tv, num_audio)

print(f"The total amount is {total_amount:.2f} Baht.")
