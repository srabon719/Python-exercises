import random


def roll_dice(sides):
    return random.randint(1, sides)


maximum = int(input("Enter the number of sides on the dice: "))

result = 0

while result != maximum:
    result = roll_dice(maximum)
    print(result)