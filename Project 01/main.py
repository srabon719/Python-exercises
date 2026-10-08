import json
import os
from item import Item
from player import Player
from room import Room


def display_text_file(filename: str):
    """Reads and prints content from a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"[Notice: {filename} was not found.]")


def build_world():
    """Constructs the default map, exits, and starting items."""
    park = Room(
        "Ramna Park",
        "A lush central park with walking tracks.",
        "You picked up discarded wrappers. The park looks pristine!"
    )
    river = Room(
        "Buriganga River",
        "The historic riverbank facing heavy industrial waste.",
        "You removed floating debris. The water looks noticeably cleaner!"
    )
    street = Room(
        "Mirpur Street",
        "A bustling street filled with rickshaws and street vendors.",
        "You swept litter off the sidewalks. The street is tidy!"
    )
    garden = Room(
        "Botanical Garden",
        "A wide botanical sanctuary full of indigenous flora.",
        "You planted a new tree sapling. Dhaka is greener!"
    )

  
    park.set_exit("north", garden)
    park.set_exit("south", river)
    park.set_exit("east", street)

    garden.set_exit("south", park)
    river.set_exit("north", park)
    street.set_exit("west", park)

  
    park.add_item(Item("Plastic Bottle", 0.1))
    river.add_item(Item("Discarded Net", 1.2))
    street.add_item(Item("Aluminum Can", 0.15))
    garden.add_item(Item("Seedling Bag", 0.8))

    rooms = {
        "Ramna Park": park,
        "Buriganga River": river,
        "Mirpur Street": street,
        "Botanical Garden": garden
    }

    return rooms, park


def get_save_filename(player_name: str) -> str:
    """Creates a safe filename based on player's name."""
    clean_name = "".join(c for c in player_name if c.isalnum() or c in ("_", "-"))
    return f"{clean_name.lower()}_save.txt"


def save_game(player: Player, rooms: dict):
    """Saves the player status and world item state into a text file."""
    save_data = {
        "player_name": player.name,
        "location": player.location.name,
        "inventory": [
            {"name": item.name, "weight": item.weight} for item in player.items
        ],
        "rooms": {
            r_name: [
                {"name": item.name, "weight": item.weight} for item in r_obj.items
            ]
            for r_name, r_obj in rooms.items()
        }
    }

    filename = get_save_filename(player.name)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(save_data, file, indent=4)
    print(f"\nGame progress saved successfully to '{filename}'!")


def load_game(player_name: str, rooms: dict):
    """Loads game state if a saved text file exists for the player."""
    filename = get_save_filename(player_name)
    if not os.path.exists(filename):
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for r_name, item_list in data.get("rooms", {}).items():
            if r_name in rooms:
                rooms[r_name].items = [
                    Item(i["name"], i["weight"]) for i in item_list
                ]

        saved_location_name = data.get("location", "Ramna Park")
        player_location = rooms.get(saved_location_name, rooms["Ramna Park"])

        player = Player(data.get("player_name", player_name), player_location)
        player.items = [
            Item(i["name"], i["weight"]) for i in data.get("inventory", [])
        ]

        return player
    except Exception as error:
        print(f"Error loading save file: {error}")
        return None


def play_game():
    """Main game loop and player actions."""
    rooms, starting_room = build_world()

    
    player_name = input("Enter your player name: ").strip()
    if not player_name:
        player_name = "Volunteer"

    save_file = get_save_filename(player_name)
    player = None

  
    if os.path.exists(save_file):
        choice = input(f"Found save file '{save_file}'. Continue? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            player = load_game(player_name, rooms)
            print(f"\nWelcome back, {player.name}! Loaded your saved game.")

  
    if player is None:
        while True:
            age_input = input("Enter your age: ").strip()
            if age_input.isdigit():
                player_age = int(age_input)
                break
            print("Please enter a valid numeric age.")

        if player_age < 12:
            print("You must be at least 12 years old to play.")
            print("Returning to menu...")
            return

        player = Player(player_name, starting_room)
        print(f"\nWelcome to the game, {player.name}!")


    print("\nOBJECTIVE: Help clean Dhaka to reach the ending!")
    print("- Route A: Collect 3 pieces of waste/items.")
    print("- Route B: Use the 'clean' command 3 times.")

    clean_count = 0
    command = ""

    while command != "lopeta":
      
        if len(player.items) >= 3:
            print("\n" + "=" * 40)
            print("YOU WIN! (Route A - Waste Collector)")
            print("You gathered enough litter to clear the city!")
            print("=" * 40)
            break

        if clean_count >= 3:
            print("\n" + "=" * 40)
            print("YOU WIN! (Route B - City Restorer)")
            print("You cleaned enough locations to restore Dhaka!")
            print("=" * 40)
            break

      
        print("\n" + "=" * 32)
        print(f"LOCATION: {player.location.name}")
        print("Exits   :", ", ".join(player.location.exits.keys()))

        if player.location.items:
            items_str = ", ".join(str(i) for i in player.location.items)
            print(f"Items   : {items_str}")
        else:
            print("Items   : None")

        print("\n[Commands: move | clean | collect | inventory | save | lopeta]")
        command = input("Enter choice: ").strip().lower()

        if command == "move":
            direction = input(f"Direction ({'/'.join(player.location.exits.keys())}): ").strip()
            player.move(direction)

        elif command == "clean":
            clean_count += 1
            print(f"\n{player.location.clean_action_text}")
            print(f"Cleaning actions completed: {clean_count}/3")

        elif command == "collect":
            if not player.location.items:
                print("\nThere are no items to collect here.")
            else:
                item_to_pick = input("Enter item name to pick up: ").strip()
                player.collect_item(item_to_pick)

        elif command == "inventory":
            player.show_inventory()

        elif command == "save":
            save_game(player, rooms)

        elif command == "lopeta":
            save_prompt = input("Would you like to save before exiting? (y/n): ").strip().lower()
            if save_prompt in ("y", "yes"):
                save_game(player, rooms)
            print("\nReturning to main menu...")

        else:
            print("Invalid choice. Please choose an option from the menu.")


def main():
    """Main menu function (Subtask 2)."""
    while True:
        print("\n" + "=" * 25)
        print("       MAIN MENU        ")
        print("=" * 25)
        print("1. Play Game")
        print("2. Instructions & Story")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print()
            display_text_file("intro.txt")
            print()
            display_text_file("instructions.txt")
        elif choice == "3":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()