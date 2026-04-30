class Territory:
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.armies = 0
        self.neighbors = []

    def add_neighbor(self, territory):
        if territory not in self.neighbors:
            self.neighbors.append(territory)

    def set_owner(self, player):
        self.owner = player

    def add_armies(self, count):
        self.armies += count

    def remove_armies(self, count):
        if count <= self.armies:
            self.armies -= count