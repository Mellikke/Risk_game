# Form implementation generated from reading ui file 'client\\game_window.ui'
#
# Edited manually for a polished single-screen Risk-style interface.
# WARNING: If pyuic6 is run again, manual changes in this file will be lost.

from PyQt6 import QtCore, QtGui, QtWidgets


class WorldMapWidget(QtWidgets.QWidget):
    territoryClicked = QtCore.pyqtSignal(str, str, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(820, 520)
        self.base_width = 1320
        self.base_height = 940
        self.selected_name = None

        blue = QtGui.QColor("#768dca")
        red = QtGui.QColor("#965252")

        # SADECE TEK HARİTA SETİ VAR.
        # Farklı renkli eski ikinci harita tamamen kaldırıldı.
        self.territories = [
    # NORTH AMERICA
    {
        "name": "Alaska",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(35, 95), QtCore.QPointF(105, 60),
            QtCore.QPointF(170, 88), QtCore.QPointF(145, 135),
            QtCore.QPointF(75, 150), QtCore.QPointF(30, 125),
        ],
        "label_pos": QtCore.QPointF(95, 112),
        "army_pos": QtCore.QPointF(88, 78),
    },
    {
        "name": "Yukon",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(145, 75), QtCore.QPointF(245, 60),
            QtCore.QPointF(315, 92), QtCore.QPointF(285, 150),
            QtCore.QPointF(175, 160), QtCore.QPointF(145, 135),
            QtCore.QPointF(170, 88),
        ],
        "label_pos": QtCore.QPointF(230, 112),
        "army_pos": QtCore.QPointF(222, 78),
    },
    {
        "name": "Batı Kanada",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(75, 150), QtCore.QPointF(145, 135),
            QtCore.QPointF(175, 160), QtCore.QPointF(170, 225),
            QtCore.QPointF(95, 245), QtCore.QPointF(55, 195),
        ],
        "label_pos": QtCore.QPointF(118, 188),
        "army_pos": QtCore.QPointF(115, 158),
    },
    {
        "name": "Doğu Kanada",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(175, 160), QtCore.QPointF(285, 150),
            QtCore.QPointF(350, 180), QtCore.QPointF(335, 250),
            QtCore.QPointF(230, 260), QtCore.QPointF(170, 225),
        ],
        "label_pos": QtCore.QPointF(260, 205),
        "army_pos": QtCore.QPointF(255, 172),
    },
    {
        "name": "Batı Amerika",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(95, 245), QtCore.QPointF(170, 225),
            QtCore.QPointF(230, 260), QtCore.QPointF(220, 330),
            QtCore.QPointF(145, 340), QtCore.QPointF(85, 292),
        ],
        "label_pos": QtCore.QPointF(155, 285),
        "army_pos": QtCore.QPointF(152, 250),
    },
    {
        "name": "Doğu Amerika",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(230, 260), QtCore.QPointF(335, 250),
            QtCore.QPointF(365, 325), QtCore.QPointF(315, 390),
            QtCore.QPointF(220, 330),
        ],
        "label_pos": QtCore.QPointF(292, 315),
        "army_pos": QtCore.QPointF(290, 278),
    },
    {
        "name": "Orta Amerika",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(145, 340), QtCore.QPointF(220, 330),
            QtCore.QPointF(315, 390), QtCore.QPointF(280, 435),
            QtCore.QPointF(190, 420),
        ],
        "label_pos": QtCore.QPointF(232, 385),
        "army_pos": QtCore.QPointF(230, 350),
    },

    # SOUTH AMERICA
    {
        "name": "Venezuela",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(190, 420), QtCore.QPointF(280, 435),
            QtCore.QPointF(305, 475), QtCore.QPointF(245, 500),
            QtCore.QPointF(190, 470),
        ],
        "label_pos": QtCore.QPointF(245, 460),
        "army_pos": QtCore.QPointF(242, 430),
    },
    {
        "name": "Peru",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(190, 470), QtCore.QPointF(245, 500),
            QtCore.QPointF(255, 565), QtCore.QPointF(205, 560),
            QtCore.QPointF(175, 510),
        ],
        "label_pos": QtCore.QPointF(220, 525),
        "army_pos": QtCore.QPointF(218, 492),
    },
    {
        "name": "Brezilya",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(245, 500), QtCore.QPointF(305, 475),
            QtCore.QPointF(350, 530), QtCore.QPointF(330, 610),
            QtCore.QPointF(255, 565),
        ],
        "label_pos": QtCore.QPointF(300, 545),
        "army_pos": QtCore.QPointF(295, 510),
    },
    {
        "name": "Arjantin",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(255, 565), QtCore.QPointF(330, 610),
            QtCore.QPointF(300, 675), QtCore.QPointF(225, 650),
            QtCore.QPointF(205, 560),
        ],
        "label_pos": QtCore.QPointF(270, 620),
        "army_pos": QtCore.QPointF(265, 585),
    },

    # EUROPE
    {
        "name": "İzlanda",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(415, 80), QtCore.QPointF(465, 65),
            QtCore.QPointF(505, 95), QtCore.QPointF(480, 132),
            QtCore.QPointF(425, 125),
        ],
        "label_pos": QtCore.QPointF(460, 102),
        "army_pos": QtCore.QPointF(458, 72),
    },
    {
        "name": "Britanya",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(430, 155), QtCore.QPointF(490, 135),
            QtCore.QPointF(530, 175), QtCore.QPointF(505, 235),
            QtCore.QPointF(445, 225), QtCore.QPointF(415, 180),
        ],
        "label_pos": QtCore.QPointF(472, 185),
        "army_pos": QtCore.QPointF(468, 152),
    },
    {
        "name": "İskandinavya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(520, 90), QtCore.QPointF(610, 70),
            QtCore.QPointF(675, 110), QtCore.QPointF(650, 175),
            QtCore.QPointF(570, 165), QtCore.QPointF(530, 130),
        ],
        "label_pos": QtCore.QPointF(595, 125),
        "army_pos": QtCore.QPointF(590, 90),
    },
    {
        "name": "Batı Avrupa",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(505, 235), QtCore.QPointF(570, 220),
            QtCore.QPointF(595, 285), QtCore.QPointF(545, 335),
            QtCore.QPointF(480, 310), QtCore.QPointF(445, 225),
        ],
        "label_pos": QtCore.QPointF(535, 275),
        "army_pos": QtCore.QPointF(528, 240),
    },
    {
        "name": "Orta Avrupa",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(570, 165), QtCore.QPointF(650, 175),
            QtCore.QPointF(690, 230), QtCore.QPointF(650, 290),
            QtCore.QPointF(595, 285), QtCore.QPointF(570, 220),
        ],
        "label_pos": QtCore.QPointF(625, 225),
        "army_pos": QtCore.QPointF(620, 190),
    },
    {
        "name": "Balkanlar",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(650, 290), QtCore.QPointF(720, 275),
            QtCore.QPointF(760, 330), QtCore.QPointF(725, 385),
            QtCore.QPointF(660, 360), QtCore.QPointF(595, 285),
        ],
        "label_pos": QtCore.QPointF(680, 325),
        "army_pos": QtCore.QPointF(675, 292),
    },
    {
        "name": "Trakya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(690, 230), QtCore.QPointF(770, 220),
            QtCore.QPointF(805, 260), QtCore.QPointF(760, 330),
            QtCore.QPointF(720, 275),
        ],
        "label_pos": QtCore.QPointF(748, 262),
        "army_pos": QtCore.QPointF(745, 232),
    },

    # AFRICA + MIDDLE EAST
    {
        "name": "Kuzey Afrika",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(480, 310), QtCore.QPointF(545, 335),
            QtCore.QPointF(660, 360), QtCore.QPointF(620, 435),
            QtCore.QPointF(505, 430), QtCore.QPointF(455, 370),
        ],
        "label_pos": QtCore.QPointF(555, 380),
        "army_pos": QtCore.QPointF(550, 340),
    },
    {
        "name": "Mısır",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(660, 360), QtCore.QPointF(725, 385),
            QtCore.QPointF(760, 445), QtCore.QPointF(700, 480),
            QtCore.QPointF(620, 435),
        ],
        "label_pos": QtCore.QPointF(690, 425),
        "army_pos": QtCore.QPointF(685, 388),
    },
    {
        "name": "Orta Afrika",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(505, 430), QtCore.QPointF(620, 435),
            QtCore.QPointF(700, 480), QtCore.QPointF(660, 565),
            QtCore.QPointF(550, 555), QtCore.QPointF(490, 500),
        ],
        "label_pos": QtCore.QPointF(590, 500),
        "army_pos": QtCore.QPointF(585, 462),
    },
    {
        "name": "Güney Afrika",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(550, 555), QtCore.QPointF(660, 565),
            QtCore.QPointF(630, 675), QtCore.QPointF(535, 660),
            QtCore.QPointF(505, 600),
        ],
        "label_pos": QtCore.QPointF(585, 615),
        "army_pos": QtCore.QPointF(580, 575),
    },
    {
        "name": "Orta Doğu",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(760, 330), QtCore.QPointF(835, 325),
            QtCore.QPointF(870, 390), QtCore.QPointF(835, 465),
            QtCore.QPointF(760, 445), QtCore.QPointF(725, 385),
        ],
        "label_pos": QtCore.QPointF(805, 392),
        "army_pos": QtCore.QPointF(800, 352),
    },

    # ASIA
    {
        "name": "Kafkasya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(805, 260), QtCore.QPointF(890, 235),
            QtCore.QPointF(955, 270), QtCore.QPointF(935, 350),
            QtCore.QPointF(835, 325), QtCore.QPointF(760, 330),
        ],
        "label_pos": QtCore.QPointF(870, 302),
        "army_pos": QtCore.QPointF(865, 265),
    },
    {
        "name": "Ural",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(890, 235), QtCore.QPointF(965, 190),
            QtCore.QPointF(1040, 230), QtCore.QPointF(1015, 305),
            QtCore.QPointF(955, 270),
        ],
        "label_pos": QtCore.QPointF(970, 245),
        "army_pos": QtCore.QPointF(965, 210),
    },
    {
        "name": "Sibirya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(965, 190), QtCore.QPointF(1105, 170),
            QtCore.QPointF(1180, 235), QtCore.QPointF(1140, 330),
            QtCore.QPointF(1015, 305),
        ],
        "label_pos": QtCore.QPointF(1080, 250),
        "army_pos": QtCore.QPointF(1075, 210),
    },
    {
        "name": "Orta Asya",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(955, 270), QtCore.QPointF(1015, 305),
            QtCore.QPointF(1050, 390), QtCore.QPointF(975, 440),
            QtCore.QPointF(870, 390), QtCore.QPointF(835, 325),
        ],
        "label_pos": QtCore.QPointF(950, 360),
        "army_pos": QtCore.QPointF(945, 320),
    },
    {
        "name": "Çin",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(1015, 305), QtCore.QPointF(1140, 330),
            QtCore.QPointF(1165, 430), QtCore.QPointF(1085, 500),
            QtCore.QPointF(975, 440), QtCore.QPointF(1050, 390),
        ],
        "label_pos": QtCore.QPointF(1080, 400),
        "army_pos": QtCore.QPointF(1075, 360),
    },
    {
        "name": "Hindistan",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(870, 390), QtCore.QPointF(975, 440),
            QtCore.QPointF(970, 545), QtCore.QPointF(890, 535),
            QtCore.QPointF(835, 465),
        ],
        "label_pos": QtCore.QPointF(910, 475),
        "army_pos": QtCore.QPointF(905, 438),
    },
    {
        "name": "Güneydoğu Asya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(970, 545), QtCore.QPointF(1085, 500),
            QtCore.QPointF(1135, 565), QtCore.QPointF(1070, 635),
            QtCore.QPointF(985, 610),
        ],
        "label_pos": QtCore.QPointF(1045, 565),
        "army_pos": QtCore.QPointF(1040, 525),
    },
    {
        "name": "Japonya",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(1180, 235), QtCore.QPointF(1245, 260),
            QtCore.QPointF(1230, 350), QtCore.QPointF(1165, 430),
            QtCore.QPointF(1140, 330),
        ],
        "label_pos": QtCore.QPointF(1195, 330),
        "army_pos": QtCore.QPointF(1190, 290),
    },

    # AUSTRALIA / OCEANIA
    {
        "name": "Endonezya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(985, 610), QtCore.QPointF(1070, 635),
            QtCore.QPointF(1120, 700), QtCore.QPointF(1045, 735),
            QtCore.QPointF(965, 690),
        ],
        "label_pos": QtCore.QPointF(1040, 680),
        "army_pos": QtCore.QPointF(1035, 642),
    },
    {
        "name": "Yeni Gine",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(1120, 700), QtCore.QPointF(1215, 675),
            QtCore.QPointF(1275, 735), QtCore.QPointF(1195, 785),
            QtCore.QPointF(1045, 735),
        ],
        "label_pos": QtCore.QPointF(1165, 730),
        "army_pos": QtCore.QPointF(1160, 695),
    },
    {
        "name": "Batı Avustralya",
        "owner": "Player 2",
        "armies": 3,
        "color": blue,
        "points": [
            QtCore.QPointF(1010, 775), QtCore.QPointF(1115, 750),
            QtCore.QPointF(1180, 820), QtCore.QPointF(1130, 910),
            QtCore.QPointF(1015, 890), QtCore.QPointF(965, 825),
        ],
        "label_pos": QtCore.QPointF(1070, 825),
        "army_pos": QtCore.QPointF(1065, 785),
    },
    {
        "name": "Doğu Avustralya",
        "owner": "Player 1",
        "armies": 3,
        "color": red,
        "points": [
            QtCore.QPointF(1115, 750), QtCore.QPointF(1260, 770),
            QtCore.QPointF(1300, 850), QtCore.QPointF(1210, 920),
            QtCore.QPointF(1130, 910), QtCore.QPointF(1180, 820),
        ],
        "label_pos": QtCore.QPointF(1210, 835),
        "army_pos": QtCore.QPointF(1205, 795),
    },
]

        self.paths = {}
        self._build_paths()

    def _build_paths(self):
        self.paths.clear()

        for territory in self.territories:
            path = QtGui.QPainterPath()
            points = territory["points"]

            path.moveTo(points[0])
            for point in points[1:]:
                path.lineTo(point)

            path.closeSubpath()
            self.paths[territory["name"]] = path

    def _view_transform(self):
        scale = min(self.width() / self.base_width, self.height() / self.base_height)
        x_offset = (self.width() - self.base_width * scale) / 2
        y_offset = (self.height() - self.base_height * scale) / 2
        return scale, x_offset, y_offset

    def _screen_to_world(self, pos):
        scale, x_offset, y_offset = self._view_transform()

        return QtCore.QPointF(
            (pos.x() - x_offset) / scale,
            (pos.y() - y_offset) / scale
        )

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        self._draw_background(painter)

        scale, x_offset, y_offset = self._view_transform()
        painter.translate(x_offset, y_offset)
        painter.scale(scale, scale)

        self._draw_sea_routes(painter)
        self._draw_territories(painter)
        self._draw_labels(painter)

    def _draw_background(self, painter):
        gradient = QtGui.QRadialGradient(
            QtCore.QPointF(self.width() / 2, self.height() / 2),
            max(self.width(), self.height()) * 0.82
        )
        gradient.setColorAt(0.0, QtGui.QColor("#2bbbe2"))
        gradient.setColorAt(0.42, QtGui.QColor("#1186b1"))
        gradient.setColorAt(1.0, QtGui.QColor("#063a54"))

        painter.fillRect(self.rect(), gradient)

        grid_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 18), 1)
        painter.setPen(grid_pen)

        step = 45
        for x in range(0, self.width(), step):
            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), step):
            painter.drawLine(0, y, self.width(), y)

        diagonal_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 10), 1)
        painter.setPen(diagonal_pen)

        for i in range(-self.height(), self.width(), 95):
            painter.drawLine(i, 0, i + self.height(), self.height())

        for i in range(0, self.width() + self.height(), 125):
            painter.drawLine(i, 0, i - self.height(), self.height())

    def _draw_sea_routes(self, painter):
        pos = {t["name"]: t["army_pos"] for t in self.territories}

        sea_routes = [
            ("Alaska", "Kamçatka"),
            ("Grönland", "İzlanda"),
            ("Brezilya", "Kuzey Afrika"),
            ("Güney Avrupa", "Mısır"),
            ("Orta Dogu", "Doğu Afrika"),
            ("Siam", "Endonezya"),
            ("Endonezya", "Yeni Gine"),
            ("Yeni Gine", "Doğu Avustralya"),
            ("Batı Avustralya", "Doğu Avustralya"),
        ]

        glow_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 70), 7)
        glow_pen.setStyle(QtCore.Qt.PenStyle.DotLine)
        glow_pen.setCapStyle(QtCore.Qt.PenCapStyle.RoundCap)

        route_pen = QtGui.QPen(QtGui.QColor(245, 250, 255, 230), 2.8)
        route_pen.setStyle(QtCore.Qt.PenStyle.DotLine)
        route_pen.setCapStyle(QtCore.Qt.PenCapStyle.RoundCap)

        node_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 210), 1.5)
        node_brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 230))

        for a, b in sea_routes:
            if a not in pos or b not in pos:
                continue

            start = pos[a]
            end = pos[b]

            control = QtCore.QPointF(
                (start.x() + end.x()) / 2,
                (start.y() + end.y()) / 2 - 42
            )

        path = QtGui.QPainterPath()
        path.moveTo(start)
        path.quadTo(control, end)

        painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
        painter.setPen(glow_pen)
        painter.drawPath(path)

        painter.setPen(route_pen)
        painter.drawPath(path)

        # iki uçtaki küçük beyaz bağlantı noktaları
        painter.setPen(node_pen)
        painter.setBrush(node_brush)
        painter.drawEllipse(start, 3, 3)
        painter.drawEllipse(end, 3, 3)

    def _draw_territories(self, painter):
        for territory in self.territories:
            name = territory["name"]
            path = self.paths[name]
            fill_color = territory["color"]

            # Hafif gölge
            painter.save()
            painter.translate(3, 4)
            painter.setBrush(QtGui.QColor(0, 0, 0, 95))
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.drawPath(path)
            painter.restore()

            # Seçili bölge parlaması
            if self.selected_name == name:
                painter.setPen(QtGui.QPen(QtGui.QColor(255, 230, 130, 145), 11))
                painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
                painter.drawPath(path)
                border_pen = QtGui.QPen(QtGui.QColor("#ffe284"), 4.5)
            else:
                border_pen = QtGui.QPen(QtGui.QColor("#0a1720"), 3.2)

            painter.setBrush(fill_color)
            painter.setPen(border_pen)
            painter.drawPath(path)

            # Üst ışık / iç parlama
            painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 35), 1.5))
            painter.drawPath(path)

    def _draw_labels(self, painter):
        for territory in self.territories:
            name = territory["name"]
            armies = territory["armies"]
            fill_color = territory["color"]

            army_pos = territory["army_pos"]
            label_pos = territory["label_pos"]

            # Aynı rengin koyu/açık tonları
            outer_color = QtGui.QColor(fill_color).darker(145)
            inner_color = QtGui.QColor(fill_color)
            highlight_color = QtGui.QColor(fill_color).lighter(135)

            # Dış gölge
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.setBrush(QtGui.QColor(0, 0, 0, 95))
            painter.drawEllipse(
                QtCore.QPointF(army_pos.x() + 2.5, army_pos.y() + 3),
                22, 22
            )

            # Dış halka
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 150), 2.2))
            painter.setBrush(outer_color)
            painter.drawEllipse(army_pos, 21, 21)

            # İç disk
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 80), 1.4))
            painter.setBrush(inner_color)
            painter.drawEllipse(army_pos, 17, 17)

            # Üst parlama (kabartma hissi)
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.setBrush(QtGui.QColor(highlight_color.red(), highlight_color.green(), highlight_color.blue(), 120))
            painter.drawEllipse(
                QtCore.QPointF(army_pos.x() - 4, army_pos.y() - 5),
                8, 6
            )

            # Asker sayısı
            army_font = QtGui.QFont("Segoe UI", 11)
            army_font.setBold(True)
            painter.setFont(army_font)
            painter.setPen(QtGui.QColor("white"))
            painter.drawText(
                QtCore.QRectF(army_pos.x() - 18, army_pos.y() - 18, 36, 36),
                QtCore.Qt.AlignmentFlag.AlignCenter,
                str(armies)
            )

            # Sadece bölge adı
            label_rect = QtCore.QRectF(label_pos.x() - 52, label_pos.y() - 12, 104, 24)

            painter.setBrush(QtGui.QColor(0, 0, 0, 95))
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 45), 1))
            painter.drawRoundedRect(label_rect, 7, 7)

            label_font = QtGui.QFont("Segoe UI Semibold", 6)
            painter.setFont(label_font)
            painter.setPen(QtGui.QColor("white"))
            painter.drawText(
                label_rect,
                QtCore.Qt.AlignmentFlag.AlignCenter,
                name
            )
            

    def mousePressEvent(self, event):
        world_pos = self._screen_to_world(event.position())

        for territory in self.territories:
            name = territory["name"]

            if self.paths[name].contains(world_pos):
                self.selected_name = name
                self.territoryClicked.emit(
                    name,
                    territory["owner"],
                    territory["armies"]
                )
                self.update()
                return

        super().mousePressEvent(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 920)

        MainWindow.setStyleSheet("""
QMainWindow {
    background-color: #080908;
}

QWidget#centralwidget {
    background-color: qlineargradient(
        spread: pad,
        x1: 0.5,
        y1: 0,
        x2: 0.5,
        y2: 1,
        stop: 0 #161a16,
        stop: 1 #050505
    );
}

QGroupBox {
    border: 1px solid #3f483f;
    border-radius: 10px;
    margin-top: 18px;
    background-color: rgba(10, 16, 10, 225);
    color: #d6af5b;
    font-weight: bold;
    font-family: "Segoe UI Semibold";
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
}

QLabel {
    color: #ececec;
    font-size: 14px;
}

QLabel#resultLabel {
    background-color: #060907;
    border: 1px solid #283028;
    border-radius: 10px;
    padding: 14px;
    color: #a6c3a5;
    font-family: "Consolas";
    font-size: 15px;
}

QPushButton {
    background-color: #232823;
    border: 1px solid #465046;
    color: #ececec;
    border-radius: 8px;
    padding: 10px;
    font-weight: bold;
    font-size: 15px;
}

QPushButton:hover {
    background-color: #313931;
    border: 1px solid #d6af5b;
}

QPushButton:pressed {
    background-color: #171b17;
}

QListWidget {
    background-color: rgba(0, 0, 0, 0.15);
    border: 1px solid #313831;
    border-radius: 8px;
    color: #ececec;
    font-size: 14px;
    padding: 6px;
}

QFrame#mapFrame {
    background-color: #0b3c57;
    border: 2px solid #d6af5b;
    border-radius: 10px;
}

QFrame#diceFrame {
    background-color: #101510;
    border: 1px solid #2d352d;
    border-radius: 8px;
}
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(16, 14, 16, 14)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName("mainLayout")

        # HEADER
        self.headerFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 90))
        self.headerFrame.setObjectName("headerFrame")

        self.headerContent = QtWidgets.QVBoxLayout(self.headerFrame)
        self.headerContent.setContentsMargins(0, 0, 0, 0)
        self.headerContent.setSpacing(4)
        self.headerContent.setObjectName("headerContent")

        self.titleLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.titleLabel.setStyleSheet(
            "font-size: 38px; "
            "font-weight: 800; "
            "color: #d6af5b; "
            "letter-spacing: 12px;"
        )
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.headerContent.addWidget(self.titleLabel)

        self.playerInfoLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.playerInfoLabel.setStyleSheet(
            "font-size: 15px; "
            "color: #ff5656; "
            "font-style: italic;"
        )
        self.playerInfoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.playerInfoLabel.setObjectName("playerInfoLabel")
        self.headerContent.addWidget(self.playerInfoLabel)

        self.mainLayout.addWidget(self.headerFrame)

        # MIDDLE AREA
        self.gameAreaLayout = QtWidgets.QHBoxLayout()
        self.gameAreaLayout.setSpacing(12)
        self.gameAreaLayout.setObjectName("gameAreaLayout")

        # LEFT STATUS PANEL
        self.statusGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.statusGroupBox.setMinimumSize(QtCore.QSize(235, 0))
        self.statusGroupBox.setMaximumWidth(260)
        self.statusGroupBox.setObjectName("statusGroupBox")

        self.statusLayout = QtWidgets.QVBoxLayout(self.statusGroupBox)
        self.statusLayout.setContentsMargins(14, 16, 14, 14)
        self.statusLayout.setSpacing(12)
        self.statusLayout.setObjectName("statusLayout")

        self.currentPlayerLabel = QtWidgets.QLabel(parent=self.statusGroupBox)
        self.currentPlayerLabel.setObjectName("currentPlayerLabel")
        self.statusLayout.addWidget(self.currentPlayerLabel)

        self.phaseLabel = QtWidgets.QLabel(parent=self.statusGroupBox)
        self.phaseLabel.setObjectName("phaseLabel")
        self.statusLayout.addWidget(self.phaseLabel)

        self.reinforcementLabel = QtWidgets.QLabel(parent=self.statusGroupBox)
        self.reinforcementLabel.setStyleSheet("color: #31ff6b; font-weight: bold;")
        self.reinforcementLabel.setObjectName("reinforcementLabel")
        self.statusLayout.addWidget(self.reinforcementLabel)

        self.statusHintLabel = QtWidgets.QLabel(parent=self.statusGroupBox)
        self.statusHintLabel.setWordWrap(True)
        self.statusHintLabel.setStyleSheet("color: #b7c7b7; font-size: 13px;")
        self.statusHintLabel.setObjectName("statusHintLabel")
        self.statusLayout.addWidget(self.statusHintLabel)

        spacerItem = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.statusLayout.addItem(spacerItem)

        self.legendFrame = QtWidgets.QFrame(parent=self.statusGroupBox)
        self.legendFrame.setObjectName("legendFrame")

        self.legendLayout = QtWidgets.QVBoxLayout(self.legendFrame)
        self.legendLayout.setContentsMargins(0, 0, 0, 0)
        self.legendLayout.setSpacing(8)
        self.legendLayout.setObjectName("legendLayout")

        self.p1LegendLabel = QtWidgets.QLabel(parent=self.legendFrame)
        self.p1LegendLabel.setStyleSheet("color: #ff4747; font-weight: bold;")
        self.p1LegendLabel.setObjectName("p1LegendLabel")
        self.legendLayout.addWidget(self.p1LegendLabel)

        self.p2LegendLabel = QtWidgets.QLabel(parent=self.legendFrame)
        self.p2LegendLabel.setStyleSheet("color: #4f7bff; font-weight: bold;")
        self.p2LegendLabel.setObjectName("p2LegendLabel")
        self.legendLayout.addWidget(self.p2LegendLabel)

        self.statusLayout.addWidget(self.legendFrame)
        self.gameAreaLayout.addWidget(self.statusGroupBox)

        # MAP PANEL
        self.mapFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.mapFrame.setObjectName("mapFrame")
        self.mapFrame.setMinimumSize(QtCore.QSize(840, 560))

        self.mapFrameLayout = QtWidgets.QVBoxLayout(self.mapFrame)
        self.mapFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mapFrameLayout.setSpacing(0)
        self.mapFrameLayout.setObjectName("mapFrameLayout")

        self.worldMapWidget = WorldMapWidget(parent=self.mapFrame)
        self.mapFrameLayout.addWidget(self.worldMapWidget)

        # Eski app.py uyumluluğu için gizli butonlar.
        self.trakyaButton = QtWidgets.QPushButton(parent=self.mapFrame)
        self.anadoluButton = QtWidgets.QPushButton(parent=self.mapFrame)
        self.kafkasyaButton = QtWidgets.QPushButton(parent=self.mapFrame)
        self.balkanlarButton = QtWidgets.QPushButton(parent=self.mapFrame)
        self.ortaDoguButton = QtWidgets.QPushButton(parent=self.mapFrame)
        self.kuzeyAfrikaButton = QtWidgets.QPushButton(parent=self.mapFrame)

        hidden_buttons = [
            self.trakyaButton,
            self.anadoluButton,
            self.kafkasyaButton,
            self.balkanlarButton,
            self.ortaDoguButton,
            self.kuzeyAfrikaButton,
        ]

        for button in hidden_buttons:
            button.hide()

        self.worldMapWidget.territoryClicked.connect(self._handle_map_click)

        self.gameAreaLayout.addWidget(self.mapFrame)

        # RIGHT COMMAND PANEL
        self.attackGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.attackGroupBox.setMinimumSize(QtCore.QSize(310, 0))
        self.attackGroupBox.setMaximumWidth(340)
        self.attackGroupBox.setObjectName("attackGroupBox")

        self.attackLayout = QtWidgets.QVBoxLayout(self.attackGroupBox)
        self.attackLayout.setContentsMargins(14, 16, 14, 14)
        self.attackLayout.setSpacing(12)
        self.attackLayout.setObjectName("attackLayout")

        self.attackerLabel = QtWidgets.QLabel(parent=self.attackGroupBox)
        self.attackerLabel.setObjectName("attackerLabel")
        self.attackLayout.addWidget(self.attackerLabel)

        self.defenderLabel = QtWidgets.QLabel(parent=self.attackGroupBox)
        self.defenderLabel.setObjectName("defenderLabel")
        self.attackLayout.addWidget(self.defenderLabel)

        self.commandHintLabel = QtWidgets.QLabel(parent=self.attackGroupBox)
        self.commandHintLabel.setWordWrap(True)
        self.commandHintLabel.setStyleSheet("color: #b7c7b7; font-size: 13px;")
        self.commandHintLabel.setObjectName("commandHintLabel")
        self.attackLayout.addWidget(self.commandHintLabel)

        self.territoryList = QtWidgets.QListWidget(parent=self.attackGroupBox)
        self.territoryList.setObjectName("territoryList")
        self.territoryList.setMinimumHeight(280)
        self.territoryList.setStyleSheet("""
        QListWidget {
            background-color: rgba(0, 0, 0, 0.22);
            border: 1px solid #36413f;
            border-radius: 10px;
            color: #f0f0f0;
            font-size: 12px;
            padding: 8px;
        }

        QListWidget::item {
            padding: 7px;
            margin: 2px;
            border-radius: 6px;
        }

        QListWidget::item:selected {
            background-color: #d4b067;
            color: #111;
        }
        """)
        self.attackLayout.addWidget(self.territoryList)

        self.diceFrame = QtWidgets.QFrame(parent=self.attackGroupBox)
        self.diceFrame.setMinimumSize(QtCore.QSize(0, 70))
        self.diceFrame.setObjectName("diceFrame")

        self.diceLayout = QtWidgets.QHBoxLayout(self.diceFrame)
        self.diceLayout.setContentsMargins(10, 10, 10, 10)
        self.diceLayout.setSpacing(12)
        self.diceLayout.setObjectName("diceLayout")

        self.diceInfoLabel = QtWidgets.QLabel(parent=self.diceFrame)
        self.diceInfoLabel.setStyleSheet("color: #d8d8d8; font-size: 13px;")
        self.diceInfoLabel.setObjectName("diceInfoLabel")
        self.diceLayout.addWidget(self.diceInfoLabel)

        self.attackLayout.addWidget(self.diceFrame)

        self.gameAreaLayout.addWidget(self.attackGroupBox)

        self.gameAreaLayout.setStretch(0, 1)
        self.gameAreaLayout.setStretch(1, 5)
        self.gameAreaLayout.setStretch(2, 1)

        self.mainLayout.addLayout(self.gameAreaLayout)

        # BOTTOM AREA
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setSpacing(12)
        self.bottomLayout.setObjectName("bottomLayout")

        self.resultLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultLabel.setMinimumSize(QtCore.QSize(0, 90))
        self.resultLabel.setObjectName("resultLabel")
        self.bottomLayout.addWidget(self.resultLabel)

        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setObjectName("buttonLayout")

        self.attackButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.attackButton.setMinimumSize(QtCore.QSize(260,44))
        self.attackButton.setStyleSheet(
            "background-color: #7a1111; "
            "border: 1px solid #ff4d4d; "
            "font-size: 17px;"
        )
        self.attackButton.setObjectName("attackButton")
        self.buttonLayout.addWidget(self.attackButton)

        self.nextTurnButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nextTurnButton.setMinimumSize(QtCore.QSize(260, 44))
        self.nextTurnButton.setStyleSheet(
            "background-color: #0f5e1c; "
            "border: 1px solid #45ff73; "
            "font-size: 17px;"
        )
        self.nextTurnButton.setObjectName("nextTurnButton")
        self.buttonLayout.addWidget(self.nextTurnButton)

        self.bottomLayout.addLayout(self.buttonLayout)

        self.bottomLayout.setStretch(0, 3)
        self.bottomLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.bottomLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _handle_map_click(self, name, owner, armies):
        self.resultLabel.setText(
            f"[SYSTEM]: {name} seçildi | Owner: {owner} | Armies: {armies}"
        )
        self.attackerLabel.setText(f"FROM: {name}")

        mapping = {
            "Trakya": self.trakyaButton,
            "Anadolu": self.anadoluButton,
            "Kafkasya": self.kafkasyaButton,
            "Balkanlar": self.balkanlarButton,
            "Orta Doğu": self.ortaDoguButton,
            "Kuzey Afrika": self.kuzeyAfrikaButton,
        }

        if name in mapping:
            mapping[name].click()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "RISK: Global Tactics"))

        self.titleLabel.setText(_translate("MainWindow", "RISK GAME"))
        self.playerInfoLabel.setText(_translate("MainWindow", "Oyuncu: Player 2"))

        self.statusGroupBox.setTitle(_translate("MainWindow", "TACTICAL STATUS"))
        self.currentPlayerLabel.setText(_translate("MainWindow", "Sıradaki Oyuncu: Player 1"))
        self.phaseLabel.setText(_translate("MainWindow", "Aşama: Reinforcement"))
        self.reinforcementLabel.setText(_translate("MainWindow", "Takviye Asker: 3"))

        self.statusHintLabel.setText(
            _translate(
                "MainWindow",
                "Haritadan bir bölge seçerek işlem başlatabilirsin."
            )
        )

        self.p1LegendLabel.setText(_translate("MainWindow", "● P1: Red Division"))
        self.p2LegendLabel.setText(_translate("MainWindow", "● P2: Blue Division"))

        self.attackGroupBox.setTitle(_translate("MainWindow", "COMMAND CENTER"))
        self.attackerLabel.setText(_translate("MainWindow", "FROM: None"))
        self.defenderLabel.setText(_translate("MainWindow", "TARGET: None"))

        self.commandHintLabel.setText(
            _translate(
                "MainWindow",
                "Bir bölge seç, ardından saldırı hedefini belirle."
            )
        )

        self.diceInfoLabel.setText(_translate("MainWindow", "Dice / Combat Info"))

        self.resultLabel.setText(_translate("MainWindow", "[SYSTEM]: Waiting for action..."))

        self.attackButton.setText(_translate("MainWindow", "SALDIR"))
        self.nextTurnButton.setText(_translate("MainWindow", "TURU BİTİR"))

        # Gizli butonlar mevcut app.py bağlantıları bozulmasın diye duruyor.
        self.trakyaButton.setText(_translate("MainWindow", "Trakya"))
        self.anadoluButton.setText(_translate("MainWindow", "Anadolu"))
        self.kafkasyaButton.setText(_translate("MainWindow", "Kafkasya"))
        self.balkanlarButton.setText(_translate("MainWindow", "Balkanlar"))
        self.ortaDoguButton.setText(_translate("MainWindow", "Orta Dogu"))
        self.kuzeyAfrikaButton.setText(_translate("MainWindow", "Kuzey Afrika"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())