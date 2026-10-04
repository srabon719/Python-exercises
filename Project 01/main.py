from item import Item
from player import Player
from room import Room


def build_world():
  """Creates rooms, connects exits, and places initial items."""
  park = Room(
      "Ramna Park",
      "A lush central park with walking tracks.",
      "You picked up discarded wrappers. The park looks pristine!",
  )
  river = Room(
      "Buriganga River",
      "The historic riverbank facing heavy industrial waste.",
      "You removed floating debris. The water looks noticeably cleaner!",
  )
  street = Room(
      "Mirpur Street",
      "A bustling street filled with rickshaws and street vendors.",
      "You swept litter off the sidewalks. The street is tidy!",
  )
  garden = Room(
      "Botanical Garden",
      "A wide botanical sanctuary full of indigenous flora.",
      "You planted a new tree sapling. Dhaka is greener!",
  )

  # Connect room exits
  park.set_exit("north", garden)
  park.set_exit("south", river)
  park.set_exit("east", street)

  garden.set_exit("south", park)
  river.set_exit("north", park)
  street.set_exit("west", park)

  # Distribute items
  park.add_item(Item("Plastic Bottle", 0.1))
  river.add_item(Item("Discarded Net", 1.2))
  street.add_item(Item("Aluminum Can", 0.15))
  garden.add_item(Item("Seedling Bag", 0.8))

  return park


def main():
  player_name = input("Enter your name: ").strip()

  while True:
    age_input = input("Enter your age: ").strip()
    if age_input.isdigit():
      player_age = int(age_input)
      break
    print("Please enter a valid numeric age.")

  if player_age < 12:
    print("You are a minor under the age of 12.")
    print("The game is shutting down.")
    return

  # Create initial player and world objects
  starting_room = build_world()
  player = Player(player_name, starting_room)

  print(f"\nWelcome to the game, {player.name}!")
  print("Your objective is to explore and make Dhaka cleaner and greener.")
  print(f"Starting location: {player.location.name}")
  print(player.location.description)

  command = ""
  while command != "lopeta":
    print("\n" + "=" * 30)
    print(f"CURRENT LOCATION: {player.location.name}")
    print("Available exits:", ", ".join(player.location.exits.keys()))

    if player.location.items:
      items_str = ", ".join(str(i) for i in player.location.items)
      print(f"Items here: {items_str}")
    else:
      print("Items here: None")

    print("\nCOMMANDS:")
    print("  move      - Move to an adjacent area")
    print("  clean     - Perform environmental cleanup")
    print("  collect   - Collect an item from this area")
    print("  inventory - View collected items")
    print("  lopeta    - Exit the game")

    command = input("Enter your choice: ").strip().lower()

    if command == "move":
      direction = input(
          f"Enter direction ({'/'.join(player.location.exits.keys())}): "
      ).strip()
      player.move(direction)

    elif command == "clean":
      print(f"\n{player.location.clean_action_text}")

    elif command == "collect":
      if not player.location.items:
        print("\nThere are no items to collect here.")
      else:
        item_to_pick = input("Enter the name of the item to collect: ").strip()
        player.collect_item(item_to_pick)

    elif command == "inventory":
      player.show_inventory()

    elif command == "lopeta":
      print("\nThank you for playing and helping clean Dhaka!")

    else:
      print("Invalid choice. Please choose an option from the menu.")


if __name__ == "__main__":
  main()