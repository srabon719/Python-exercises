player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor under the age of 12.")
    print("The game is shutting down.")
else:
    print("Welcome to the game,", player_name + "!")
    print("Your objective is to help make Dhaka cleaner and greener city.")

    command = ""
    while command != "lopeta":
        print("MAIN MENU")
        print("park - Clean a park")
        print("river - Clean the Buriganga River")
        print("street - Clean a street")
        print("garden - Plant a tree in a garden")
        print("lopeta - Exit the game")

        command = input("Enter your command: ")

        if command == "park":
            print("You have chosen to clean a park.")
            print("Cleaning the park...")
            print("The park is now clean and beautiful!")
        elif command == "river":
            print("You have chosen to clean the Buriganga River.")
            print("Cleaning the river...")
            print("The Buriganga River is now clean and healthy!")
        elif command == "street":
            print("You have chosen to clean a street.")
            print("Cleaning the street...")
            print("The street is now clean and safe!")
        elif command == "garden":
            print("You have chosen to plant a tree in a garden.")
            print("Planting the tree...")
            print("The garden is now greener and more beautiful!")
        elif command == "lopeta":
            print("Exiting the game. Thank you for helping Dhaka,", player_name + "!")

