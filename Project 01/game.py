inventory = []


def clean_park():
    print("\nYou cleaned a park.")
    print("The park is now clean and beautiful!")


def clean_river():
    print("\nYou cleaned the Buriganga River.")
    print("The river is now cleaner!")


def clean_street():
    print("\nYou cleaned a street.")
    print("The street is now clean!")


def plant_tree():
    print("\nYou planted a tree in a garden.")
    print("Dhaka is now greener!")


def collect_item():
    item = input("\nEnter the name of the item you found: ")
    inventory.append(item)
    print(item, "was added to your inventory.")


def show_inventory():
    print("\nYour inventory:")

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(item)


player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor under the age of 12.")
    print("The game is shutting down.")

else:
    print("\nWelcome to the game,", player_name + "!")
    print("Your objective is to help make Dhaka a cleaner and greener city.")

    command = ""

    while command != "lopeta":
        print("\nMAIN MENU")
        print("park - Clean a park")
        print("river - Clean the Buriganga River")
        print("street - Clean a street")
        print("garden - Plant a tree")
        print("collect - Collect an item")
        print("inventory - Show collected items")
        print("lopeta - Exit the game")

        command = input("Enter your choice: ").lower()

        if command == "park":
            clean_park()

        elif command == "river":
            clean_river()

        elif command == "street":
            clean_street()

        elif command == "garden":
            plant_tree()

        elif command == "collect":
            collect_item()

        elif command == "inventory":
            show_inventory()

        elif command == "lopeta":
            print("Thank you for playing!")

        else:
            print("Invalid choice. Please try again.")