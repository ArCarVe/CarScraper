

class Car:

    def __init__(self, modification, is_automatic, seats, doors, hp):
        self.modification = modification
        self.is_automatic = is_automatic
        self.seats = seats
        self.doors = doors
        self.hp = hp

    def to_json(self):
        return {
            "modification": self.modification,
            "isAutomatic": self.is_automatic,
            "seats": self.seats,
            "doors": self.doors,
            "hp": self.hp
        }
