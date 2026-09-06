import random

correct_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != correct_number:
    if guess > correct_number:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Guess again: "))

print("Correct")