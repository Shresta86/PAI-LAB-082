class Room:
    def __init__(self, name, is_dirty=True):
        self.name = name
        self.is_dirty = is_dirty
        self.neighbors = []

    def connect(self, other_room):
        """Connect this room to another room (bi-directional)."""
        self.neighbors.append(other_room)
        other_room.neighbors.append(self)

class VacuumCleaner:
    def __init__(self, start_room):
        self.current_room = start_room
        self.visited = set()

    def clean_room(self, room):
        if room.is_dirty:
            room.is_dirty = False
            print(f"Cleaned {room.name}")
        else:
            print(f"{room.name} is already clean")

    def dfs_clean(self, room=None):
        """Recursive DFS to clean all rooms."""
        if room is None:
            room = self.current_room

        self.visited.add(room)
        self.current_room = room
        self.clean_room(room)

        for neighbor in room.neighbors:
            if neighbor not in self.visited:
                print(f"Moving from {room.name} to {neighbor.name}")
                self.dfs_clean(neighbor)

# Example Usage
living_room = Room("Living Room")
kitchen = Room("Kitchen")
bedroom = Room("Bedroom")
bathroom = Room("Bathroom")

# Connect rooms
living_room.connect(kitchen)
kitchen.connect(bedroom)
bedroom.connect(bathroom)

# Start vacuum
vacuum = VacuumCleaner(living_room)
vacuum.dfs_clean()
