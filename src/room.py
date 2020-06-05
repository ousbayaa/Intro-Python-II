# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
 #      self.n_to = None
 #      self.s_to = None
 #      self.e_to = None
 #      self.w_to = None
        if items == None:
            self.items = None
        else:
            self.items = self.init_items(items)

    def __str__(self):
        return f"{self.name}: {self.description}"

    def init_items(self, items):
        return [Item(name, description) for name, description in items]


