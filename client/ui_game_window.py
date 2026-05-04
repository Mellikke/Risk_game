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
        self.base_width = 1000
        self.base_height = 540
        self.selected_name = None

        blue = QtGui.QColor("#768dca")
        red = QtGui.QColor("#965252")

        # SADECE TEK HARİTA SETİ VAR.
        # Farklı renkli eski ikinci harita tamamen kaldırıldı.
        self.territories = [
            {
                "name": "Alaska",
                "owner": "Player 2",
                "armies": 2,
                "color": blue,
                "points": [
                    QtCore.QPointF(35, 95),
                    QtCore.QPointF(105, 60),
                    QtCore.QPointF(175, 88),
                    QtCore.QPointF(155, 150),
                    QtCore.QPointF(75, 165),
                    QtCore.QPointF(30, 130),
                ],
                "label_pos": QtCore.QPointF(102, 122),
                "army_pos": QtCore.QPointF(90, 92),
            },
            {
                "name": "Kanada",
                "owner": "Player 2",
                "armies": 3,
                "color": blue,
                "points": [
                    QtCore.QPointF(155, 72),
                    QtCore.QPointF(285, 55),
                    QtCore.QPointF(370, 92),
                    QtCore.QPointF(340, 165),
                    QtCore.QPointF(225, 182),
                    QtCore.QPointF(155, 150),
                    QtCore.QPointF(175, 88),
                ],
                "label_pos": QtCore.QPointF(250, 120),
                "army_pos": QtCore.QPointF(240, 92),
            },
            {
                "name": "Doğu Amerika",
                "owner": "Player 2",
                "armies": 4,
                "color": blue,
                "points": [
                    QtCore.QPointF(75, 165),
                    QtCore.QPointF(155, 150),
                    QtCore.QPointF(225, 182),
                    QtCore.QPointF(340, 165),
                    QtCore.QPointF(365, 245),
                    QtCore.QPointF(315, 322),
                    QtCore.QPointF(200, 320),
                    QtCore.QPointF(118, 250),
                ],
                "label_pos": QtCore.QPointF(225, 242),
                "army_pos": QtCore.QPointF(210, 204),
            },
            {
                "name": "Güney Amerika",
                "owner": "Player 1",
                "armies": 2,
                "color": red,
                "points": [
                    QtCore.QPointF(205, 320),
                    QtCore.QPointF(315, 322),
                    QtCore.QPointF(365, 430),
                    QtCore.QPointF(315, 515),
                    QtCore.QPointF(225, 500),
                    QtCore.QPointF(188, 405),
                ],
                "label_pos": QtCore.QPointF(275, 430),
                "army_pos": QtCore.QPointF(265, 388),
            },
            {
                "name": "Batı Avrupa",
                "owner": "Player 2",
                "armies": 2,
                "color": blue,
                "points": [
                    QtCore.QPointF(430, 130),
                    QtCore.QPointF(505, 108),
                    QtCore.QPointF(555, 148),
                    QtCore.QPointF(535, 220),
                    QtCore.QPointF(462, 235),
                    QtCore.QPointF(405, 180),
                ],
                "label_pos": QtCore.QPointF(480, 178),
                "army_pos": QtCore.QPointF(472, 145),
            },
            {
                "name": "Balkanlar",
                "owner": "Player 2",
                "armies": 3,
                "color": blue,
                "points": [
                    QtCore.QPointF(530, 118),
                    QtCore.QPointF(605, 108),
                    QtCore.QPointF(660, 138),
                    QtCore.QPointF(648, 205),
                    QtCore.QPointF(570, 216),
                    QtCore.QPointF(532, 172),
                ],
                "label_pos": QtCore.QPointF(590, 168),
                "army_pos": QtCore.QPointF(590, 135),
            },
            {
                "name": "Trakya",
                "owner": "Player 2",
                "armies": 3,
                "color": blue,
                "points": [
                    QtCore.QPointF(600, 78),
                    QtCore.QPointF(675, 72),
                    QtCore.QPointF(720, 104),
                    QtCore.QPointF(660, 138),
                    QtCore.QPointF(605, 108),
                ],
                "label_pos": QtCore.QPointF(656, 106),
                "army_pos": QtCore.QPointF(656, 78),
            },
            {
                "name": "Kafkasya",
                "owner": "Player 1",
                "armies": 3,
                "color": red,
                "points": [
                    QtCore.QPointF(720, 104),
                    QtCore.QPointF(810, 88),
                    QtCore.QPointF(900, 132),
                    QtCore.QPointF(874, 220),
                    QtCore.QPointF(792, 208),
                    QtCore.QPointF(660, 138),
                ],
                "label_pos": QtCore.QPointF(790, 165),
                "army_pos": QtCore.QPointF(785, 128),
            },
            {
                "name": "Anadolu",
                "owner": "Player 1",
                "armies": 4,
                "color": red,
                "points": [
                    QtCore.QPointF(532, 172),
                    QtCore.QPointF(648, 205),
                    QtCore.QPointF(792, 208),
                    QtCore.QPointF(770, 315),
                    QtCore.QPointF(625, 335),
                    QtCore.QPointF(505, 260),
                ],
                "label_pos": QtCore.QPointF(655, 245),
                "army_pos": QtCore.QPointF(650, 205),
            },
            {
                "name": "Kuzey Afrika",
                "owner": "Player 2",
                "armies": 3,
                "color": blue,
                "points": [
                    QtCore.QPointF(405, 238),
                    QtCore.QPointF(505, 260),
                    QtCore.QPointF(625, 335),
                    QtCore.QPointF(588, 420),
                    QtCore.QPointF(470, 438),
                    QtCore.QPointF(390, 350),
                ],
                "label_pos": QtCore.QPointF(505, 338),
                "army_pos": QtCore.QPointF(498, 298),
            },
            {
                "name": "Orta Doğu",
                "owner": "Player 1",
                "armies": 3,
                "color": red,
                "points": [
                    QtCore.QPointF(625, 335),
                    QtCore.QPointF(770, 315),
                    QtCore.QPointF(860, 350),
                    QtCore.QPointF(845, 430),
                    QtCore.QPointF(705, 462),
                    QtCore.QPointF(588, 420),
                ],
                "label_pos": QtCore.QPointF(720, 390),
                "army_pos": QtCore.QPointF(715, 350),
            },
            {
                "name": "Asya",
                "owner": "Player 1",
                "armies": 5,
                "color": red,
                "points": [
                    QtCore.QPointF(810, 88),
                    QtCore.QPointF(948, 115),
                    QtCore.QPointF(985, 210),
                    QtCore.QPointF(970, 322),
                    QtCore.QPointF(860, 350),
                    QtCore.QPointF(770, 315),
                    QtCore.QPointF(792, 208),
                    QtCore.QPointF(874, 220),
                    QtCore.QPointF(900, 132),
                ],
                "label_pos": QtCore.QPointF(905, 230),
                "army_pos": QtCore.QPointF(905, 190),
            },
            {
                "name": "Avustralya",
                "owner": "Player 2",
                "armies": 2,
                "color": blue,
                "points": [
                    QtCore.QPointF(820, 410),
                    QtCore.QPointF(925, 395),
                    QtCore.QPointF(975, 455),
                    QtCore.QPointF(945, 520),
                    QtCore.QPointF(842, 515),
                    QtCore.QPointF(790, 455),
                ],
                "label_pos": QtCore.QPointF(885, 465),
                "army_pos": QtCore.QPointF(880, 430),
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
        gradient = QtGui.QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QtGui.QColor("#2aa7d4"))
        gradient.setColorAt(0.50, QtGui.QColor("#0f6e96"))
        gradient.setColorAt(1.0, QtGui.QColor("#083c57"))

        painter.fillRect(self.rect(), gradient)

        grid_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 28), 1)
        painter.setPen(grid_pen)

        step = 42

        for x in range(0, self.width(), step):
            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), step):
            painter.drawLine(0, y, self.width(), y)

        diagonal_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 17), 1)
        painter.setPen(diagonal_pen)

        for i in range(-self.height(), self.width(), 80):
            painter.drawLine(i, 0, i + self.height(), self.height())

    def _draw_sea_routes(self, painter):
        route_pen = QtGui.QPen(QtGui.QColor(255, 255, 255, 140), 3)
        route_pen.setStyle(QtCore.Qt.PenStyle.DashLine)

        painter.setPen(route_pen)
        painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)

        routes = [
            (QtCore.QPointF(340, 165), QtCore.QPointF(430, 148)),
            (QtCore.QPointF(305, 355), QtCore.QPointF(405, 345)),
            (QtCore.QPointF(845, 430), QtCore.QPointF(810, 455)),
            (QtCore.QPointF(770, 315), QtCore.QPointF(820, 320)),
        ]

        for start, end in routes:
            path = QtGui.QPainterPath()
            path.moveTo(start)

            control = QtCore.QPointF(
                (start.x() + end.x()) / 2,
                (start.y() + end.y()) / 2 - 25
            )

            path.quadTo(control, end)
            painter.drawPath(path)

    def _draw_territories(self, painter):
        for territory in self.territories:
            name = territory["name"]
            path = self.paths[name]

            painter.setBrush(territory["color"])

            if self.selected_name == name:
                painter.setPen(QtGui.QPen(QtGui.QColor(255, 240, 168, 120), 10))
                painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
                painter.drawPath(path)

                pen = QtGui.QPen(QtGui.QColor("#fff0a8"), 5)
            else:
                 pen = QtGui.QPen(QtGui.QColor("#092028"), 3)

            painter.setBrush(territory["color"])
            painter.setPen(pen)
            painter.drawPath(path)

            # Hafif iç parlama
            painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 35), 2))
            painter.drawPath(path)

    def _draw_labels(self, painter):
        for territory in self.territories:
            name = territory["name"]
            owner = territory["owner"]
            armies = territory["armies"]

            army_pos = territory["army_pos"]
            label_pos = territory["label_pos"]

            # Army marker
            painter.setBrush(QtGui.QColor(18, 18, 18, 205))
            painter.setPen(QtGui.QPen(QtGui.QColor("white"), 2))
            painter.drawEllipse(army_pos, 15, 15)

            army_font = QtGui.QFont("Segoe UI", 9)
            army_font.setBold(True)
            painter.setFont(army_font)
            painter.setPen(QtGui.QColor("white"))
            painter.drawText(
                QtCore.QRectF(army_pos.x() - 15, army_pos.y() - 15, 30, 30),
                QtCore.Qt.AlignmentFlag.AlignCenter,
                str(armies)
            )

            # Oyuncu kısaltması
            owner_short = "P1" if owner == "Player 1" else "P2"

            # Territory name box
            label_rect = QtCore.QRectF(label_pos.x() - 58, label_pos.y() - 17, 116, 36)

            painter.setBrush(QtGui.QColor(0, 0, 0, 88))
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 65), 1))
            painter.drawRoundedRect(label_rect, 8, 8)

            label_font = QtGui.QFont("Segoe UI", 8)
            label_font.setBold(True)
            painter.setFont(label_font)
            painter.setPen(QtGui.QColor("white"))
            painter.drawText(
                label_rect,
                QtCore.Qt.AlignmentFlag.AlignCenter,
                f"{name}\n{owner_short} - {armies}"
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
            border: 1px solid #3b443b;
            border-radius: 8px;
            color: #ececec;
            font-size: 12px;
            padding: 6px;
        }

        QListWidget::item {
            padding: 6px;
            margin: 2px;
            border-radius: 5px;
        }

        QListWidget::item:selected {
            background-color: #c5a059;
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