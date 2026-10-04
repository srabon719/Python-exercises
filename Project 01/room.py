class Room:

  def __init__(
      self, name: str, description: str, clean_action_text: str = ""
  ):
    self.name = name
    self.description = description
    self.clean_action_text = clean_action_text
    self.items = []
    self.exits = {}

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item_name: str):
    """Removes an item from the room by name and returns it."""
    for item in self.items:
      if item.name.lower() == item_name.lower():
        self.items.remove(item)
        return item
    return None

  def set_exit(self, direction: str, neighbor_room):
    """Connects an exit direction to another Room object."""
    self.exits[direction.lower()] = neighbor_room