numbers = []

while True:
    number = input("Enter a number or press Enter to quit: ")

    if number == "":
        break

    numbers.append(float(number))

numbers.sort(reverse=True)

print("The five greatest numbers:")

for number in numbers[:5]:
    print(number)