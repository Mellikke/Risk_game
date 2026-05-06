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
            # =========================
            # NORTH AMERICA
            # =========================
            ("Alaska", "Kuzeybatı Toprakları"),
            ("Alaska", "Alberta"),
            ("Alaska", "Kamçatka"),  # wrap-around / dünya yuvarlaklığı

            ("Kuzeybatı Toprakları", "Alberta"),
            ("Kuzeybatı Toprakları", "Ontario"),
            ("Kuzeybatı Toprakları", "Grönland"),

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

            # Deniz bağlantısı
            ("Doğu ABD", "Kuzey Afrika"),

            # =========================
            # SOUTH AMERICA
            # =========================
            ("Orta Amerika", "Venezuela"),

            ("Venezuela", "Peru"),
            ("Venezuela", "Brezilya"),

            ("Peru", "Brezilya"),
            ("Peru", "Arjantin"),

            ("Brezilya", "Arjantin"),

            # Deniz bağlantısı
            ("Brezilya", "Güney Afrika"),

            # =========================
            # EUROPE
            # =========================
            ("İzlanda", "Büyük Britanya"),
            ("İzlanda", "İskandinavya"),

            ("Büyük Britanya", "Batı Avrupa"),
            ("Büyük Britanya", "Kuzey Avrupa"),

            ("İskandinavya", "Kuzey Avrupa"),
            ("İskandinavya", "Ukrayna"),

            ("Kuzey Avrupa", "Batı Avrupa"),
            ("Kuzey Avrupa", "Güney Avrupa"),
            ("Kuzey Avrupa", "Ukrayna"),

            ("Batı Avrupa", "Güney Avrupa"),
            ("Batı Avrupa", "Kuzey Afrika"),

            ("Güney Avrupa", "Kuzey Afrika"),
            ("Güney Avrupa", "Mısır"),
            ("Güney Avrupa", "Orta Dogu"),
            ("Güney Avrupa", "Ukrayna"),

            ("Ukrayna", "Ural"),
            ("Ukrayna", "Afganistan"),
            ("Ukrayna", "Orta Dogu"),

            # Deniz bağlantısı
            ("Quebec", "Büyük Britanya"),

            # =========================
            # AFRICA
            # =========================
            ("Kuzey Afrika", "Mısır"),
            ("Kuzey Afrika", "Kongo"),
            ("Kuzey Afrika", "Güney Avrupa"),
            ("Kuzey Afrika", "Batı Avrupa"),

            ("Mısır", "Orta Dogu"),
            ("Mısır", "Doğu Afrika"),
            ("Mısır", "Kongo"),

            ("Kongo", "Doğu Afrika"),
            ("Kongo", "Güney Afrika"),

            ("Doğu Afrika", "Orta Dogu"),
            ("Doğu Afrika", "Güney Afrika"),

            ("Güney Afrika", "Madagaskar"),

            # Deniz bağlantısı
            ("Doğu Afrika", "Madagaskar"),

            # =========================
            # ASIA
            # =========================
            ("Ural", "Sibirya"),
            ("Ural", "Afganistan"),
            ("Ural", "Çin"),
            ("Ural", "Ukrayna"),

            ("Sibirya", "Yakutsk"),
            ("Sibirya", "Irkutsk"),
            ("Sibirya", "Ural"),

            ("Yakutsk", "Sibirya"),
            ("Yakutsk", "Irkutsk"),
            ("Yakutsk", "Kamçatka"),

            ("Kamçatka", "Yakutsk"),
            ("Kamçatka", "Irkutsk"),
            ("Kamçatka", "Japonya"),
            ("Kamçatka", "Alaska"),

            ("Irkutsk", "Sibirya"),
            ("Irkutsk", "Yakutsk"),
            ("Irkutsk", "Kamçatka"),
            ("Irkutsk", "Japonya"),
            ("Irkutsk", "Moğolistan"),

            ("Japonya", "Kamçatka"),
            ("Japonya", "Irkutsk"),
            ("Japonya", "Çin"),

            ("Afganistan", "Ukrayna"),
            ("Afganistan", "Ural"),
            ("Afganistan", "Orta Dogu"),
            ("Afganistan", "Hindistan"),
            ("Afganistan", "Çin"),
            ("Afganistan", "Moğolistan"),

            ("Moğolistan", "Afganistan"),
            ("Moğolistan", "Çin"),
            ("Moğolistan", "Irkutsk"),

            ("Çin", "Ural"),
            ("Çin", "Afganistan"),
            ("Çin", "Moğolistan"),
            ("Çin", "Hindistan"),
            ("Çin", "Siam"),
            ("Çin", "Japonya"),

            ("Orta Dogu", "Ukrayna"),
            ("Orta Dogu", "Güney Avrupa"),
            ("Orta Dogu", "Mısır"),
            ("Orta Dogu", "Doğu Afrika"),
            ("Orta Dogu", "Afganistan"),
            ("Orta Dogu", "Hindistan"),

            ("Hindistan", "Orta Dogu"),
            ("Hindistan", "Afganistan"),
            ("Hindistan", "Çin"),
            ("Hindistan", "Siam"),

            ("Siam", "Hindistan"),
            ("Siam", "Çin"),
            ("Siam", "Endonezya"),

            # Deniz bağlantısı
            ("Siam", "Yeni Gine"),

            # =========================
            # AUSTRALIA / OCEANIA
            # =========================
            ("Endonezya", "Siam"),
            ("Endonezya", "Yeni Gine"),
            ("Endonezya", "Batı Avustralya"),

            ("Yeni Gine", "Endonezya"),
            ("Yeni Gine", "Batı Avustralya"),
            ("Yeni Gine", "Doğu Avustralya"),

            ("Batı Avustralya", "Endonezya"),
            ("Batı Avustralya", "Yeni Gine"),
            ("Batı Avustralya", "Doğu Avustralya"),

            ("Doğu Avustralya", "Yeni Gine"),
            ("Doğu Avustralya", "Batı Avustralya"),
        ]
        for territory1, territory2 in connections:
            self.add_connection(territory1, territory2)