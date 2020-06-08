# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, items=[]):
        self.current_room = location
        self.name = None
        self.items = items

    def takeItem(self, item):
        self.items.append(item)
        print("You took ", item)
    
    def dropItem(self, item):
        self.items.remove(item)
        print("You dropped ", item)