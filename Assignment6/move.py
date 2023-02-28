class Move:
    # Constructor to initialize a Move object with player, x-coordinate and y-coordinate
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    # Return a string representation of the object
    def __repr__(self):
        return "Move()"

    def __str__(self):
        return f"[{self.x}, {self.y}]"