import random

dice_amount = int(input("How many dice do you want to roll? "))

total = 0

for i in range(dice_amount):
    result = random.randint(1, 6)
    total = total + result

print("The sum of the dice is:", total)