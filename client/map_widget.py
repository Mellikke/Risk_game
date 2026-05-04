from PyQt6 import QtCore, QtGui, QtWidgets


class WorldMapWidget(QtWidgets.QWidget):
    territoryClicked = QtCore.pyqtSignal(str, str, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(760, 520)
        self.selected_territory = None

        self.territories = [
            {
                "name": "North America",
                "owner": "Player 2",
                "armies": 3,
                "color": QtGui.QColor("#d7c63f"),
                "label_pos": QtCore.QPointF(120, 130),
                "army_pos": QtCore.QPointF(120, 95),
                "points": [
                    QtCore.QPointF(40, 70), QtCore.QPointF(130, 40), QtCore.QPointF(235, 65),
                    QtCore.QPointF(270, 120), QtCore.QPointF(230, 180), QtCore.QPointF(150, 210),
                    QtCore.QPointF(80, 180), QtCore.QPointF(45, 120)
                ]
            },
            {
                "name": "South America",
                "owner": "Player 1",
                "armies": 2,
                "color": QtGui.QColor("#d63d67"),
                "label_pos": QtCore.QPointF(190, 345),
                "army_pos": QtCore.QPointF(190, 310),
                "points": [
                    QtCore.QPointF(180, 220), QtCore.QPointF(240, 245), QtCore.QPointF(270, 320),
                    QtCore.QPointF(250, 430), QtCore.QPointF(210, 490), QtCore.QPointF(165, 450),
                    QtCore.QPointF(150, 360), QtCore.QPointF(155, 270)
                ]
            },
            {
                "name": "Europe",
                "owner": "Player 2",
                "armies": 2,
                "color": QtGui.QColor("#7c59d6"),
                "label_pos": QtCore.QPointF(365, 120),
                "army_pos": QtCore.QPointF(365, 90),
                "points": [
                    QtCore.QPointF(320, 65), QtCore.QPointF(395, 55), QtCore.QPointF(445, 85),
                    QtCore.QPointF(435, 145), QtCore.QPointF(375, 170), QtCore.QPointF(320, 135),
                    QtCore.QPointF(300, 95)
                ]
            },
            {
                "name": "Africa",
                "owner": "Player 1",
                "armies": 3,
                "color": QtGui.QColor("#d28734"),
                "label_pos": QtCore.QPointF(395, 285),
                "army_pos": QtCore.QPointF(395, 245),
                "points": [
                    QtCore.QPointF(350, 170), QtCore.QPointF(420, 180), QtCore.QPointF(470, 245),
                    QtCore.QPointF(455, 360), QtCore.QPointF(405, 450), QtCore.QPointF(345, 415),
                    QtCore.QPointF(320, 300), QtCore.QPointF(330, 220)
                ]
            },
            {
                "name": "Asia",
                "owner": "Player 1",
                "armies": 6,
                "color": QtGui.QColor("#5fb64f"),
                "label_pos": QtCore.QPointF(610, 165),
                "army_pos": QtCore.QPointF(610, 125),
                "points": [
                    QtCore.QPointF(430, 80), QtCore.QPointF(550, 40), QtCore.QPointF(710, 55),
                    QtCore.QPointF(840, 120), QtCore.QPointF(860, 210), QtCore.QPointF(800, 265),
                    QtCore.QPointF(690, 255), QtCore.QPointF(610, 300), QtCore.QPointF(510, 260),
                    QtCore.QPointF(450, 200)
                ]
            },
            {
                "name": "Australia",
                "owner": "Player 2",
                "armies": 4,
                "color": QtGui.QColor("#b05ae5"),
                "label_pos": QtCore.QPointF(760, 400),
                "army_pos": QtCore.QPointF(760, 365),
                "points": [
                    QtCore.QPointF(690, 330), QtCore.QPointF(790, 320), QtCore.QPointF(855, 360),
                    QtCore.QPointF(835, 440), QtCore.QPointF(740, 470), QtCore.QPointF(680, 430),
                    QtCore.QPointF(665, 375)
                ]
            }
        ]

        self.paths = []
        self._build_paths()

    def _build_paths(self):
        self.paths = []
        for territory in self.territories:
            path = QtGui.QPainterPath()
            pts = territory["points"]
            path.moveTo(pts[0])
            for p in pts[1:]:
                path.lineTo(p)
            path.closeSubpath()
            self.paths.append(path)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        # Okyanus arka planı
        ocean_gradient = QtGui.QLinearGradient(0, 0, 0, self.height())
        ocean_gradient.setColorAt(0.0, QtGui.QColor("#25a8d2"))
        ocean_gradient.setColorAt(0.45, QtGui.QColor("#0b6f98"))
        ocean_gradient.setColorAt(1.0, QtGui.QColor("#08445e"))
        painter.fillRect(self.rect(), ocean_gradient)

        # Hafif grid
        pen_grid = QtGui.QPen(QtGui.QColor(255, 255, 255, 25), 1)
        painter.setPen(pen_grid)
        step = 35
        for x in range(0, self.width(), step):
            painter.drawLine(x, 0, x, self.height())
        for y in range(0, self.height(), step):
            painter.drawLine(0, y, self.width(), y)

        # Deniz yolları
        route_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 160), 2)
        route_pen.setStyle(QtCore.Qt.PenStyle.DashLine)
        painter.setPen(route_pen)
        painter.drawLine(250, 130, 300, 110)  # NA -> Europe
        painter.drawLine(250, 250, 320, 250)  # SA -> Africa
        painter.drawLine(435, 100, 440, 100)  # Europe -> Asia
        painter.drawLine(470, 320, 560, 255)  # Africa -> Asia
        painter.drawLine(690, 300, 715, 340)  # Asia -> Australia

        # Bölgeler
        for i, territory in enumerate(self.territories):
            path = self.paths[i]

            fill_color = territory["color"]
            painter.setBrush(fill_color)

            if self.selected_territory == territory["name"]:
                pen = QtGui.QPen(QtGui.QColor("#fff2a6"), 5)
            else:
                pen = QtGui.QPen(QtGui.QColor("#12242d"), 3)

            painter.setPen(pen)
            painter.drawPath(path)

            # Ordu dairesi
            army_pos = territory["army_pos"]
            painter.setBrush(QtGui.QColor(20, 20, 20, 180))
            painter.setPen(QtGui.QPen(QtGui.QColor("white"), 2))
            painter.drawEllipse(QtCore.QPointF(army_pos.x(), army_pos.y()), 18, 18)

            painter.setPen(QtGui.QColor("white"))
            font = QtGui.QFont("Segoe UI", 10)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(
                QtCore.QRectF(army_pos.x() - 18, army_pos.y() - 18, 36, 36),
                QtCore.Qt.AlignmentFlag.AlignCenter,
                str(territory["armies"])
            )

            # Bölge adı
            name_pos = territory["label_pos"]
            font2 = QtGui.QFont("Segoe UI", 10)
            font2.setBold(True)
            painter.setFont(font2)
            painter.setPen(QtGui.QColor("white"))
            painter.drawText(
                QtCore.QRectF(name_pos.x() - 70, name_pos.y() - 15, 140, 30),
                QtCore.Qt.AlignmentFlag.AlignCenter,
                territory["name"]
            )

    def mousePressEvent(self, event):
        click_pos = event.position()
        for i, territory in enumerate(self.territories):
            if self.paths[i].contains(click_pos):
                self.selected_territory = territory["name"]
                self.territoryClicked.emit(
                    territory["name"],
                    territory["owner"],
                    territory["armies"]
                )
                self.update()
                return

        super().mousePressEvent(event)