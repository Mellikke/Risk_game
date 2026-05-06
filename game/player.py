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
        territory_count = len(self.territories)

        # Risk mantığı: minimum 3 asker, bölge sayısı arttıkça artar.
        base_reinforcement = max(3, territory_count // 3)

        # Şimdilik kart bonusu yok.
        card_bonus = 0

        self.reinforcements = base_reinforcement + card_bonus
        return self.reinforcements