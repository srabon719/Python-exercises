class Player:
    def __init__(self, name: str, starting_room):
        self.name = name
        self.location = starting_room
        self.items = []

    def move(self, direction: str):
        direction = direction.lower()
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"\nYou moved to {self.location.name}.")
            print(self.location.description)
            return True
        else:
            print("\nYou cannot go that way.")
            return False

    def collect_item(self, item_name: str):
        item = self.location.remove_item(item_name)
        if item:
            self.items.append(item)
            print(f"\nYou collected: {item.name} ({item.weight} kg)")
        else:
            print(f"\nItem '{item_name}' was not found in this area.")

    def show_inventory(self):
        print("\n--- INVENTORY ---")
        if not self.items:
            print("Your inventory is empty.")
        else:
            total_weight = sum(item.weight for item in self.items)
            for item in self.items:
                print(f"- {item.name} ({item.weight} kg)")
            print(f"Total weight: {total_weight:.2f} kg")