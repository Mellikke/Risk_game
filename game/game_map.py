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
        territory1 = self.territories.get(territory1_name)
        territory2 = self.territories.get(territory2_name)

        if territory1 is None or territory2 is None:
            raise ValueError(
                f"Bağlantı kurulamadı: {territory1_name} - {territory2_name}"
            )

        territory1.add_neighbor(territory2)
        territory2.add_neighbor(territory1)

    def create_default_map(self):
        self.territories.clear()

        names = [
            "Alaska",
            "Kanada",
            "Doğu Amerika",
            "Güney Amerika",
            "Batı Avrupa",
            "Balkanlar",
            "Trakya",
            "Kafkasya",
            "Anadolu",
            "Kuzey Afrika",
            "Orta Dogu",
            "Asya",
            "Avustralya",
        ]

        for name in names:
            self.add_territory(name)

        connections = [
            # Amerika
            ("Alaska", "Kanada"),
            ("Alaska", "Doğu Amerika"),
            ("Kanada", "Doğu Amerika"),
            ("Doğu Amerika", "Güney Amerika"),

            # Amerika - Avrupa/Afrika geçişleri
            ("Kanada", "Batı Avrupa"),
            ("Doğu Amerika", "Batı Avrupa"),
            ("Güney Amerika", "Kuzey Afrika"),

            # Avrupa
            ("Batı Avrupa", "Balkanlar"),
            ("Batı Avrupa", "Kuzey Afrika"),
            ("Balkanlar", "Trakya"),
            ("Balkanlar", "Anadolu"),
            ("Balkanlar", "Kuzey Afrika"),

            # Anadolu çevresi
            ("Trakya", "Anadolu"),
            ("Trakya", "Kafkasya"),
            ("Kafkasya", "Anadolu"),
            ("Kafkasya", "Asya"),
            ("Anadolu", "Kuzey Afrika"),
            ("Anadolu", "Orta Dogu"),
            ("Anadolu", "Asya"),

            # Afrika - Orta Doğu - Asya
            ("Kuzey Afrika", "Orta Dogu"),
            ("Orta Dogu", "Asya"),
            ("Asya", "Avustralya"),
            ("Orta Dogu", "Avustralya"),
        ]

        for territory1, territory2 in connections:
            self.add_connection(territory1, territory2)