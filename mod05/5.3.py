user_input = input("Enter a number or press Enter to quit: ")

smallest = None
largest = None

while user_input != "":
    number = float(user_input)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

    user_input = input("Enter a number or press Enter to quit: ")

if smallest is not None:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")