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
            # NORTH AMERICA
            "Alaska",
            "Kuzeybatı Toprakları",
            "Grönland",
            "Alberta",
            "Ontario",
            "Quebec",
            "Batı ABD",
            "Doğu ABD",
            "Orta Amerika",

            # SOUTH AMERICA
            "Venezuela",
            "Peru",
            "Brezilya",
            "Arjantin",

            # EUROPE
            "İzlanda",
            "Büyük Britanya",
            "İskandinavya",
            "Ukrayna",
            "Kuzey Avrupa",
            "Batı Avrupa",
            "Güney Avrupa",

            # AFRICA
            "Kuzey Afrika",
            "Mısır",
            "Doğu Afrika",
            "Kongo",
            "Güney Afrika",
            "Madagaskar",

            # ASIA
            "Ural",
            "Sibirya",
            "Yakutsk",
            "Kamçatka",
            "Irkutsk",
            "Moğolistan",
            "Japonya",
            "Afganistan",
            "Orta Dogu",
            "Hindistan",
            "Siam",
            "Çin",

            # AUSTRALIA
            "Endonezya",
            "Yeni Gine",
            "Batı Avustralya",
            "Doğu Avustralya",
        ]

        for name in names:
            self.add_territory(name)

        connections = [
            # NORTH AMERICA
            ("Alaska", "Kuzeybatı Toprakları"),
            ("Alaska", "Alberta"),
            ("Alaska", "Kamçatka"),

            ("Kuzeybatı Toprakları", "Alberta"),
            ("Kuzeybatı Toprakları", "Ontario"),
            ("Kuzeybatı Toprakları", "Grönland"),

            ("Grönland", "Ontario"),
            ("Grönland", "Quebec"),
            ("Grönland", "İzlanda"),

            ("Alberta", "Ontario"),
            ("Alberta", "Batı ABD"),

            ("Ontario", "Quebec"),
            ("Ontario", "Batı ABD"),
            ("Ontario", "Doğu ABD"),

            ("Quebec", "Doğu ABD"),

            ("Batı ABD", "Doğu ABD"),
            ("Batı ABD", "Orta Amerika"),

            ("Doğu ABD", "Orta Amerika"),

            # SOUTH AMERICA
            ("Orta Amerika", "Venezuela"),

            ("Venezuela", "Peru"),
            ("Venezuela", "Brezilya"),

            ("Peru", "Brezilya"),
            ("Peru", "Arjantin"),

            ("Brezilya", "Arjantin"),
            ("Brezilya", "Kuzey Afrika"),

            # EUROPE
            ("İzlanda", "Büyük Britanya"),
            ("İzlanda", "İskandinavya"),

            ("Büyük Britanya", "İskandinavya"),
            ("Büyük Britanya", "Kuzey Avrupa"),
            ("Büyük Britanya", "Batı Avrupa"),

            ("İskandinavya", "Kuzey Avrupa"),
            ("İskandinavya", "Ukrayna"),

            ("Ukrayna", "Kuzey Avrupa"),
            ("Ukrayna", "Güney Avrupa"),
            ("Ukrayna", "Ural"),
            ("Ukrayna", "Afganistan"),
            ("Ukrayna", "Orta Dogu"),

            ("Kuzey Avrupa", "Batı Avrupa"),
            ("Kuzey Avrupa", "Güney Avrupa"),

            ("Batı Avrupa", "Güney Avrupa"),
            ("Batı Avrupa", "Kuzey Afrika"),

            ("Güney Avrupa", "Kuzey Afrika"),
            ("Güney Avrupa", "Mısır"),
            ("Güney Avrupa", "Orta Dogu"),

            # AFRICA
            ("Kuzey Afrika", "Mısır"),
            ("Kuzey Afrika", "Doğu Afrika"),
            ("Kuzey Afrika", "Kongo"),

            ("Mısır", "Doğu Afrika"),
            ("Mısır", "Orta Dogu"),

            ("Doğu Afrika", "Kongo"),
            ("Doğu Afrika", "Güney Afrika"),
            ("Doğu Afrika", "Madagaskar"),
            ("Doğu Afrika", "Orta Dogu"),

            ("Kongo", "Güney Afrika"),

            ("Güney Afrika", "Madagaskar"),

            # ASIA
            ("Ural", "Sibirya"),
            ("Ural", "Çin"),
            ("Ural", "Afganistan"),

            ("Sibirya", "Yakutsk"),
            ("Sibirya", "Irkutsk"),
            ("Sibirya", "Moğolistan"),
            ("Sibirya", "Çin"),

            ("Yakutsk", "Kamçatka"),
            ("Yakutsk", "Irkutsk"),

            ("Kamçatka", "Irkutsk"),
            ("Kamçatka", "Moğolistan"),
            ("Kamçatka", "Japonya"),

            ("Irkutsk", "Moğolistan"),

            ("Moğolistan", "Japonya"),
            ("Moğolistan", "Çin"),

            ("Afganistan", "Orta Dogu"),
            ("Afganistan", "Hindistan"),
            ("Afganistan", "Çin"),

            ("Orta Dogu", "Hindistan"),

            ("Hindistan", "Çin"),
            ("Hindistan", "Siam"),

            ("Siam", "Çin"),
            ("Siam", "Endonezya"),

            # AUSTRALIA
            ("Endonezya", "Yeni Gine"),
            ("Endonezya", "Batı Avustralya"),

            ("Yeni Gine", "Batı Avustralya"),
            ("Yeni Gine", "Doğu Avustralya"),

            ("Batı Avustralya", "Doğu Avustralya"),
        ]

        for territory1, territory2 in connections:
            self.add_connection(territory1, territory2)