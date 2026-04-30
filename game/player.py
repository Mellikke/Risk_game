class Player:
    def __init__(self, player_id, name, color):
        self.player_id = player_id
        self.name = name
        self.color = color
        self.territories = []
        self.reinforcements = 0

    def add_territory(self, territory):
        if territory not in self.territories:
            self.territories.append(territory)

    def remove_territory(self, territory):
        if territory in self.territories:
            self.territories.remove(territory)

    def calculate_reinforcements(self):
        count = len(self.territories) // 3
        if count < 3:
            count = 3

        self.reinforcements = count