# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, name):
        self.current_room = location
        self.name = name
