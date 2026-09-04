import random
def dice_roll(sides):
    roll = random.randint(1, sides)
    return roll
sides = int(input("Number of sides:"))
while True:
    roll = dice_roll(sides)
    print(roll)
    if roll== 6:
        break

