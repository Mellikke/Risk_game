from game.territory import Territory


class GameMap:
    def __init__(self):
        self.territories = {}

    def add_territory(self, name):
        territory = Territory(name)
        self.territories[name] = territory
        return territory

    def get_territory(self, name):
        return self.territories.get(name)

    def add_connection(self, territory1_name, territory2_name):
        territory1 = self.territories[territory1_name]
        territory2 = self.territories[territory2_name]

        territory1.add_neighbor(territory2)
        territory2.add_neighbor(territory1)

    def create_default_map(self):
        names = [
            "Anadolu",
            "Trakya",
            "Kafkasya",
            "Balkanlar",
            "Orta Dogu",
            "Kuzey Afrika"
        ]

        for name in names:
            self.add_territory(name)

        self.add_connection("Anadolu", "Trakya")
        self.add_connection("Anadolu", "Kafkasya")
        self.add_connection("Anadolu", "Orta Dogu")
        self.add_connection("Trakya", "Balkanlar")
        self.add_connection("Orta Dogu", "Kuzey Afrika")
        self.add_connection("Balkanlar", "Kuzey Afrika")