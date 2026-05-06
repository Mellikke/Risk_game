import sys
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtWidgets, QtCore

from ui_game_window import Ui_MainWindow
from game.game_engine import GameEngine


class TroopTransferDialog(QtWidgets.QDialog):
    def __init__(self, from_name, to_name, max_armies, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Asker Aktarımı")
        self.setModal(True)
        self.setFixedSize(430, 315)

        self.setStyleSheet("""
            QDialog {
                background-color: #08120f;
                border: 2px solid #d4af37;
                border-radius: 16px;
            }

            QLabel#titleLabel {
                color: #d4af37;
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 2px;
            }

            QLabel#sectionLabel {
                color: #d7c48a;
                font-size: 13px;
                font-weight: bold;
            }

            QLabel.infoBox {
                background-color: #101d18;
                border: 1px solid #3a4b43;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 14px;
                font-weight: bold;
            }

            QLabel#fromBox {
                background-color: #2b1111;
                border: 1px solid #a43a3a;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 14px;
                font-weight: bold;
            }

            QLabel#toBox {
                background-color: #0d1f36;
                border: 1px solid #3b82f6;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 14px;
                font-weight: bold;
            }

            QLabel#maxLabel {
                color: #c7d3c7;
                font-size: 13px;
            }

            QLabel#valueLabel {
                color: #38ff8c;
                font-size: 30px;
                font-weight: bold;
                background-color: #0e1f18;
                border: 1px solid #1f8f63;
                border-radius: 12px;
                padding: 8px;
            }

            QSlider::groove:horizontal {
                height: 10px;
                background: #1b2a24;
                border-radius: 5px;
            }

            QSlider::sub-page:horizontal {
                background: #38ff8c;
                border-radius: 5px;
            }

            QSlider::handle:horizontal {
                background: #d4af37;
                width: 20px;
                margin: -6px 0;
                border-radius: 10px;
                border: 1px solid #fff0a8;
            }

            QSpinBox {
                background-color: #101d18;
                color: white;
                border: 1px solid #3a4b43;
                border-radius: 8px;
                padding: 4px;
                font-size: 18px;
                font-weight: bold;
            }

            QToolButton#arrowButton {
                background-color: #182820;
                color: #ffffff;
                border: 1px solid #3a4b43;
                font-size: 11px;
                font-weight: bold;
            }

            QToolButton#arrowButton:hover {
                background-color: #244234;
                color: #38ff8c;
                border: 1px solid #42d98c;
            }

            QToolButton#arrowButton:pressed {
                background-color: #2a5d47;
            }

            QPushButton {
                border-radius: 10px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton#cancelButton {
                background-color: #3b1d1d;
                color: #f8d7da;
                border: 1px solid #aa4444;
            }

            QPushButton#cancelButton:hover {
                background-color: #522525;
            }

            QPushButton#confirmButton {
                background-color: #0f7d2c;
                color: white;
                border: 1px solid #25d366;
            }

            QPushButton#confirmButton:hover {
                background-color: #14963a;
            }
        """)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(20, 18, 20, 18)
        main_layout.setSpacing(12)

        title = QtWidgets.QLabel("⚔ ASKER AKTARIMI")
        title.setObjectName("titleLabel")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        info_layout = QtWidgets.QGridLayout()
        info_layout.setHorizontalSpacing(12)
        info_layout.setVerticalSpacing(8)

        from_text = QtWidgets.QLabel("Kaynak Bölge")
        from_text.setObjectName("sectionLabel")

        to_text = QtWidgets.QLabel("Hedef Bölge")
        to_text.setObjectName("sectionLabel")

        from_box = QtWidgets.QLabel(from_name)
        from_box.setObjectName("fromBox")
        from_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        to_box = QtWidgets.QLabel(to_name)
        to_box.setObjectName("toBox")
        to_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        info_layout.addWidget(from_text, 0, 0)
        info_layout.addWidget(to_text, 0, 1)
        info_layout.addWidget(from_box, 1, 0)
        info_layout.addWidget(to_box, 1, 1)

        main_layout.addLayout(info_layout)

        max_label = QtWidgets.QLabel(f"Maksimum aktarılabilir asker: {max_armies}")
        max_label.setObjectName("maxLabel")
        max_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(max_label)

        self.value_label = QtWidgets.QLabel("1")
        self.value_label.setObjectName("valueLabel")
        self.value_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.value_label)

        control_layout = QtWidgets.QHBoxLayout()
        control_layout.setSpacing(12)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(max_armies)
        self.slider.setValue(1)

        self.spinbox = QtWidgets.QSpinBox()
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(max_armies)
        self.spinbox.setValue(1)
        self.spinbox.setFixedSize(76, 48)
        self.spinbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Native spinbox okları tema yüzünden görünmediği için kapatıyoruz.
        # Sağ tarafa görsel olarak net ▲ / ▼ butonları ekliyoruz.
        self.spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)

        arrow_layout = QtWidgets.QVBoxLayout()
        arrow_layout.setContentsMargins(0, 0, 0, 0)
        arrow_layout.setSpacing(2)

        self.up_button = QtWidgets.QToolButton()
        self.up_button.setObjectName("arrowButton")
        self.up_button.setText("▲")
        self.up_button.setFixedSize(30, 23)
        self.up_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.down_button = QtWidgets.QToolButton()
        self.down_button.setObjectName("arrowButton")
        self.down_button.setText("▼")
        self.down_button.setFixedSize(30, 23)
        self.down_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        arrow_layout.addWidget(self.up_button)
        arrow_layout.addWidget(self.down_button)

        spin_wrapper = QtWidgets.QFrame()
        spin_wrapper.setFixedSize(118, 52)
        spin_wrapper.setStyleSheet("""
            QFrame {
                background-color: #101d18;
                border: 1px solid #3a4b43;
                border-radius: 9px;
            }
        """)

        spin_wrapper_layout = QtWidgets.QHBoxLayout(spin_wrapper)
        spin_wrapper_layout.setContentsMargins(6, 2, 6, 2)
        spin_wrapper_layout.setSpacing(4)
        spin_wrapper_layout.addWidget(self.spinbox)
        spin_wrapper_layout.addLayout(arrow_layout)

        control_layout.addWidget(self.slider, 1)
        control_layout.addWidget(spin_wrapper)

        main_layout.addLayout(control_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()

        self.cancel_button = QtWidgets.QPushButton("İptal")
        self.cancel_button.setObjectName("cancelButton")

        self.confirm_button = QtWidgets.QPushButton("Birlikleri Taşı")
        self.confirm_button.setObjectName("confirmButton")

        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.confirm_button)

        main_layout.addLayout(button_layout)

        self.slider.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(lambda value: self.value_label.setText(str(value)))
        self.spinbox.valueChanged.connect(lambda value: self.value_label.setText(str(value)))

        self.up_button.clicked.connect(self.increase_amount)
        self.down_button.clicked.connect(self.decrease_amount)

        self.cancel_button.clicked.connect(self.reject)
        self.confirm_button.clicked.connect(self.accept)

    def increase_amount(self):
        current = self.spinbox.value()
        if current < self.spinbox.maximum():
            self.spinbox.setValue(current + 1)

    def decrease_amount(self):
        current = self.spinbox.value()
        if current > self.spinbox.minimum():
            self.spinbox.setValue(current - 1)

    def selected_amount(self):
        return self.spinbox.value()


class RiskGameWindow(QMainWindow):
    def __init__(self, player_name=None, player_role=None, network_client=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player_name = player_name
        self.player_role = player_role
        self.network_client = network_client

        self.game = GameEngine()
        self.game.setup_game()

        self.attacker_territory = None
        self.defender_territory = None

        # Fortify / asker aktarımı için seçimler
        self.fortify_from = None
        self.fortify_to = None
        self.fortify_done = False

        self.phase = "reinforcement"

        self.ui.nextTurnButton.clicked.connect(self.next_turn)
        self.ui.attackButton.clicked.connect(self.attack)
        self.ui.territoryList.itemClicked.connect(self.select_territory_from_list)

        self.connect_map_controls()
        self.update_screen()

    def connect_map_controls(self):
        if hasattr(self.ui, "worldMapWidget"):
            try:
                self.ui.worldMapWidget.territoryClicked.disconnect()
            except TypeError:
                pass

            self.ui.worldMapWidget.territoryClicked.connect(self.handle_world_map_click)

        button_connections = {
            "anadoluButton": "Anadolu",
            "trakyaButton": "Trakya",
            "kafkasyaButton": "Kafkasya",
            "balkanlarButton": "Balkanlar",
            "ortaDoguButton": "Orta Dogu",
            "kuzeyAfrikaButton": "Kuzey Afrika",
        }

        for button_name, territory_name in button_connections.items():
            if hasattr(self.ui, button_name):
                button = getattr(self.ui, button_name)
                try:
                    button.clicked.disconnect()
                except TypeError:
                    pass

                button.clicked.connect(
                    lambda checked=False, name=territory_name: self.select_territory_by_name(name)
                )

    def handle_world_map_click(self, name, owner=None, armies=None):
        backend_name = self.normalize_territory_name(name)
        self.select_territory_by_name(backend_name)

    def normalize_territory_name(self, name):
        name_map = {
            "Orta Doğu": "Orta Dogu",
            "Orta Dogu": "Orta Dogu",
        }
        return name_map.get(name, name)

    def display_territory_name(self, name):
        name_map = {
            "Orta Dogu": "Orta Doğu",
        }
        return name_map.get(name, name)

    def update_screen(self):
        current_player = self.game.get_current_player()

        if self.player_name and self.player_role:
            self.ui.playerInfoLabel.setText(
                f"Oyuncu: {self.player_name} ({self.player_role})"
            )
        else:
            self.ui.playerInfoLabel.setText("Oyuncu: Local Player")

        self.ui.currentPlayerLabel.setText(f"Sıradaki Oyuncu: {current_player.name}")
        self.ui.phaseLabel.setText(f"Aşama: {self.phase}")
        self.ui.reinforcementLabel.setText(
            f"Takviye Asker: {current_player.reinforcements}"
        )

        self.ui.territoryList.clear()

        for territory in self.game.game_map.territories.values():
            display_name = self.display_territory_name(territory.name)
            owner_short = "P1" if territory.owner.name == "Player 1" else "P2"

            self.ui.territoryList.addItem(
                f"{display_name}  |  {owner_short}  |  {territory.armies}"
            )

            self.update_hidden_button(territory)
            self.update_world_map_territory(territory)

        if hasattr(self.ui, "worldMapWidget"):
            self.ui.worldMapWidget.update()

        self.update_action_panel()

    def update_action_panel(self):
        current_player = self.game.get_current_player()

        can_attack = (
            self.phase == "attack"
            and self.attacker_territory is not None
            and self.defender_territory is not None
            and self.attacker_territory.owner == current_player
            and self.defender_territory.owner != current_player
            and self.defender_territory in self.attacker_territory.neighbors
            and self.attacker_territory.armies >= 2
        )

        self.ui.attackButton.setEnabled(can_attack)

        if self.phase == "reinforcement":
            self.ui.diceInfoLabel.setText(
                "Reinforcement Phase\n"
                "Kendi bölgene takviye asker yerleştir."
            )
            return

        if self.phase == "fortify":
            self.ui.attackButton.setEnabled(False)

            if self.fortify_done:
                self.ui.diceInfoLabel.setText(
                    "Takviye Aşaması\n"
                    "Asker aktarımı tamamlandı.\n"
                    "Turu bitirebilirsin."
                )
            elif self.fortify_from is None:
                self.ui.diceInfoLabel.setText(
                    "Takviye Aşaması\n"
                    "Asker aktaracağın kaynak bölgeyi seç.\n"
                    "Kaynak bölgede en az 2 asker olmalı."
                )
            else:
                self.ui.diceInfoLabel.setText(
                    f"Takviye Aşaması\n"
                    f"FROM: {self.display_territory_name(self.fortify_from.name)} "
                    f"({self.fortify_from.armies})\n"
                    "Hedef olarak kendi komşu bölgeni seç."
                )

            return

        if self.attacker_territory is None:
            self.ui.diceInfoLabel.setText(
                "Saldırı Aşaması\n"
                "Saldırmak için kendi bölgeni seç."
            )
            return

        attacker_name = self.display_territory_name(self.attacker_territory.name)

        if self.defender_territory is None:
            neighbors = [
                self.display_territory_name(n.name)
                for n in self.attacker_territory.neighbors
                if n.owner != current_player
            ]

            if neighbors:
                neighbor_text = ", ".join(neighbors[:4])
                if len(neighbors) > 4:
                    neighbor_text += "..."
            else:
                neighbor_text = "Saldırılabilir komşu yok."

            self.ui.diceInfoLabel.setText(
                f"FROM: {attacker_name} ({self.attacker_territory.armies})\n"
                f"Hedef seç: {neighbor_text}"
            )
            return

        defender_name = self.display_territory_name(self.defender_territory.name)

        overpower_limit = self.defender_territory.armies * 3 + 1
        can_overpower = self.attacker_territory.armies >= overpower_limit

        chance = self.estimate_conquest_chance(
            self.attacker_territory.armies,
            self.defender_territory.armies
        )

        if can_overpower:
            chance_line = "Direkt ele geçirme: MÜMKÜN"
        else:
            chance_line = f"Ele geçirme ihtimali: %{chance}"

        self.ui.diceInfoLabel.setText(
            f"FROM: {attacker_name} ({self.attacker_territory.armies})\n"
            f"TARGET: {defender_name} ({self.defender_territory.armies})\n"
            f"{chance_line}\n"
            "Saldırıya hazır."
        )

    def update_world_map_territory(self, territory):
        if not hasattr(self.ui, "worldMapWidget"):
            return

        display_name = self.display_territory_name(territory.name)

        for item in self.ui.worldMapWidget.territories:
            if item["name"] == display_name or item["name"] == territory.name:
                item["owner"] = territory.owner.name
                item["armies"] = territory.armies

                if territory.owner.name == "Player 1":
                    item["color"] = QtGui.QColor("#d7262d")
                else:
                    item["color"] = QtGui.QColor("#2d6df6")

                break

    def update_hidden_button(self, territory):
        button_names = {
            "Anadolu": "anadoluButton",
            "Trakya": "trakyaButton",
            "Kafkasya": "kafkasyaButton",
            "Balkanlar": "balkanlarButton",
            "Orta Dogu": "ortaDoguButton",
            "Kuzey Afrika": "kuzeyAfrikaButton",
        }

        button_name = button_names.get(territory.name)

        if not button_name or not hasattr(self.ui, button_name):
            return

        button = getattr(self.ui, button_name)
        button.setText(
            f"{territory.name}\n{territory.owner.name} - {territory.armies}"
        )

        if territory.owner.name == "Player 1":
            button.setStyleSheet("""
                QPushButton {
                    background-color: #b91c1c;
                    color: white;
                    border-radius: 12px;
                    font-weight: bold;
                }
            """)
        else:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #1d4ed8;
                    color: white;
                    border-radius: 12px;
                    font-weight: bold;
                }
            """)

    def next_turn(self):
        # Attack aşamasında TURU BİTİR'e basınca önce Fortify aşamasına geç.
        if self.phase == "attack":
            self.phase = "fortify"

            self.attacker_territory = None
            self.defender_territory = None
            self.fortify_from = None
            self.fortify_to = None
            self.fortify_done = False

            self.ui.attackerLabel.setText("FROM: None")
            self.ui.defenderLabel.setText("TARGET: None")
            self.ui.resultLabel.setText(
                "Result: Takviye aşamasına geçildi.\n"
                "Asker aktarmak için önce kaynak bölgeyi, sonra hedef bölgeyi seç."
            )

            self.update_screen()
            return

        # Fortify aşamasında veya reinforcement dışındaki durumlarda gerçekten sırayı değiştir.
        self.game.next_turn()
        self.game.start_turn()

        self.phase = "reinforcement"

        self.attacker_territory = None
        self.defender_territory = None
        self.fortify_from = None
        self.fortify_to = None
        self.fortify_done = False

        self.ui.attackerLabel.setText("FROM: None")
        self.ui.defenderLabel.setText("TARGET: None")
        self.ui.resultLabel.setText("Result: Yeni tur başladı, asker yerleştir.")

        self.update_screen()

    def select_territory_from_list(self, item):
        text = item.text()
        territory_name = text.split(" | ")[0]
        territory_name = self.normalize_territory_name(territory_name)
        self.select_territory_by_name(territory_name)

    def select_territory_by_name(self, territory_name):
        territory_name = self.normalize_territory_name(territory_name)

        selected = self.game.game_map.get_territory(territory_name)

        if selected is None:
            self.ui.resultLabel.setText(f"Result: Bölge bulunamadı: {territory_name}")
            return

        if hasattr(self.ui, "worldMapWidget"):
            self.ui.worldMapWidget.selected_name = self.display_territory_name(selected.name)
            self.ui.worldMapWidget.update()

        current_player = self.game.get_current_player()

        if self.phase == "reinforcement":
            self.handle_reinforcement_selection(selected, current_player)
            return

        if self.phase == "attack":
            self.handle_attack_selection(selected, current_player)
            return

        if self.phase == "fortify":
            self.handle_fortify_selection(selected, current_player)
            return

    def handle_reinforcement_selection(self, selected, current_player):
        if selected.owner != current_player:
            self.ui.resultLabel.setText("Result: Sadece kendi bölgene asker koyabilirsin.")
            return

        if current_player.reinforcements <= 0:
            self.phase = "attack"
            self.ui.resultLabel.setText("Result: Takviye bitti, saldırı aşamasına geçildi.")
            self.update_screen()
            return

        selected.add_armies(1)
        current_player.reinforcements -= 1

        self.ui.resultLabel.setText(
            f"Result: {self.display_territory_name(selected.name)} bölgesine 1 asker eklendi."
        )

        if current_player.reinforcements == 0:
            self.phase = "attack"
            self.ui.resultLabel.setText("Result: Takviye bitti, saldırı aşamasına geçildi.")

        self.update_screen()

    def handle_attack_selection(self, selected, current_player):
        if selected.owner == current_player:
            if selected.armies < 2:
                self.ui.resultLabel.setText(
                    f"Result: {self.display_territory_name(selected.name)} bölgesinde saldırmak için en az 2 asker olmalı."
                )
                self.attacker_territory = None
                self.defender_territory = None
                self.ui.attackerLabel.setText("FROM: None")
                self.ui.defenderLabel.setText("TARGET: None")
                self.update_action_panel()
                return

            self.attacker_territory = selected
            self.defender_territory = None

            display_name = self.display_territory_name(selected.name)

            self.ui.attackerLabel.setText(f"FROM: {display_name}")
            self.ui.defenderLabel.setText("TARGET: None")
            self.ui.resultLabel.setText(f"Result: Saldıran bölge seçildi: {display_name}")

            self.update_action_panel()
            return

        if self.attacker_territory is None:
            self.ui.resultLabel.setText("Result: Önce kendi bölgelerinden saldıran bir bölge seçmelisin.")
            self.update_action_panel()
            return

        if selected not in self.attacker_territory.neighbors:
            self.ui.resultLabel.setText(
                f"Result: {self.display_territory_name(self.attacker_territory.name)} ile "
                f"{self.display_territory_name(selected.name)} komşu değil."
            )
            self.defender_territory = None
            self.ui.defenderLabel.setText("TARGET: None")
            self.update_action_panel()
            return

        self.defender_territory = selected

        display_name = self.display_territory_name(selected.name)

        self.ui.defenderLabel.setText(f"TARGET: {display_name}")
        self.ui.resultLabel.setText(f"Result: Hedef bölge seçildi: {display_name}")

        self.update_action_panel()

    def handle_fortify_selection(self, selected, current_player):
        if self.fortify_done:
            self.ui.resultLabel.setText(
                "Result: Bu turda asker aktarımı zaten yapıldı. TURU BİTİR diyebilirsin."
            )
            self.update_action_panel()
            return

        if selected.owner != current_player:
            self.ui.resultLabel.setText(
                "Result: Sadece kendi bölgelerin arasında asker aktarabilirsin."
            )
            self.update_action_panel()
            return

        # 1) Kaynak bölge seçimi
        if self.fortify_from is None:
            if selected.armies < 2:
                self.ui.resultLabel.setText(
                    f"Result: {self.display_territory_name(selected.name)} bölgesinden asker aktarmak için en az 2 asker olmalı."
                )
                self.update_action_panel()
                return

            self.fortify_from = selected

            self.ui.attackerLabel.setText(
                f"FROM: {self.display_territory_name(selected.name)}"
            )
            self.ui.defenderLabel.setText("TARGET: None")
            self.ui.resultLabel.setText(
                f"Result: Kaynak bölge seçildi: {self.display_territory_name(selected.name)}.\n"
                "Şimdi hedef olarak kendi komşu bölgeni seç."
            )

            self.update_action_panel()
            return

        # 2) Hedef bölge kontrolleri
        if selected == self.fortify_from:
            self.ui.resultLabel.setText("Result: Hedef olarak farklı bir bölge seçmelisin.")
            self.update_action_panel()
            return

        if selected.owner != current_player:
            self.ui.resultLabel.setText("Result: Hedef bölge de sana ait olmalı.")
            self.update_action_panel()
            return

        if selected not in self.fortify_from.neighbors:
            self.ui.resultLabel.setText(
                f"Result: {self.display_territory_name(self.fortify_from.name)} ile "
                f"{self.display_territory_name(selected.name)} komşu değil. Asker aktarılamaz."
            )
            self.update_action_panel()
            return

        # 3) Kaç asker aktarılacağını kullanıcı özel oyun penceresinden seçsin.
        # Kaynak bölgede en az 1 asker kalmak zorundadır.
        max_movable = self.fortify_from.armies - 1

        from_name = self.display_territory_name(self.fortify_from.name)
        to_name = self.display_territory_name(selected.name)

        dialog = TroopTransferDialog(
            from_name=from_name,
            to_name=to_name,
            max_armies=max_movable,
            parent=self
        )

        if dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            self.ui.resultLabel.setText("Result: Asker aktarımı iptal edildi.")
            self.update_action_panel()
            return

        moving_armies = dialog.selected_amount()

        # 4) Aktarım işlemi
        self.fortify_from.remove_armies(moving_armies)
        selected.add_armies(moving_armies)

        self.fortify_done = True
        self.fortify_to = selected

        self.ui.attackerLabel.setText(f"FROM: {from_name}")
        self.ui.defenderLabel.setText(f"TARGET: {to_name}")

        self.ui.resultLabel.setText(
            f"Result: {moving_armies} asker {from_name} bölgesinden "
            f"{to_name} bölgesine aktarıldı.\n"
            "Şimdi TURU BİTİR diyebilirsin."
        )

        self.fortify_from = None
        self.fortify_to = None

        self.update_screen()

    def roll_risk_dice(self, attacker_armies, defender_armies):
        attack_dice_count = min(3, attacker_armies - 1)
        defend_dice_count = min(2, defender_armies)

        attack_rolls = sorted(
            [random.randint(1, 6) for _ in range(attack_dice_count)],
            reverse=True
        )

        defend_rolls = sorted(
            [random.randint(1, 6) for _ in range(defend_dice_count)],
            reverse=True
        )

        attacker_losses = 0
        defender_losses = 0

        comparisons = min(len(attack_rolls), len(defend_rolls))

        for i in range(comparisons):
            if attack_rolls[i] > defend_rolls[i]:
                defender_losses += 1
            else:
                attacker_losses += 1

        return attack_rolls, defend_rolls, attacker_losses, defender_losses

    def estimate_conquest_chance(self, attacker_armies, defender_armies, simulations=700):
        if attacker_armies < 2 or defender_armies <= 0:
            return 0.0

        wins = 0

        for _ in range(simulations):
            simulated_attacker = attacker_armies
            simulated_defender = defender_armies

            while simulated_attacker >= 2 and simulated_defender > 0:
                attack_dice_count = min(3, simulated_attacker - 1)
                defend_dice_count = min(2, simulated_defender)

                attack_rolls = sorted(
                    [random.randint(1, 6) for _ in range(attack_dice_count)],
                    reverse=True
                )

                defend_rolls = sorted(
                    [random.randint(1, 6) for _ in range(defend_dice_count)],
                    reverse=True
                )

                comparisons = min(len(attack_rolls), len(defend_rolls))

                for i in range(comparisons):
                    if attack_rolls[i] > defend_rolls[i]:
                        simulated_defender -= 1
                    else:
                        simulated_attacker -= 1

                    if simulated_attacker < 2 or simulated_defender <= 0:
                        break

            if simulated_defender <= 0:
                wins += 1

        return round((wins / simulations) * 100, 1)

    def attack(self):
        current_player = self.game.get_current_player()

        if self.phase != "attack":
            self.ui.resultLabel.setText("Result: Önce takviye askerlerini yerleştirmelisin.")
            self.update_action_panel()
            return

        if self.attacker_territory is None or self.defender_territory is None:
            self.ui.resultLabel.setText("Result: Önce FROM ve TARGET seç.")
            self.update_action_panel()
            return

        if self.attacker_territory.owner != current_player:
            self.ui.resultLabel.setText("Result: Sadece kendi bölgenle saldırabilirsin.")
            self.update_action_panel()
            return

        if self.defender_territory.owner == current_player:
            self.ui.resultLabel.setText("Result: Kendi bölgene saldıramazsın.")
            self.update_action_panel()
            return

        if self.defender_territory not in self.attacker_territory.neighbors:
            self.ui.resultLabel.setText(
                f"Result: {self.display_territory_name(self.attacker_territory.name)} ile "
                f"{self.display_territory_name(self.defender_territory.name)} komşu değil."
            )
            self.update_action_panel()
            return

        if self.attacker_territory.armies < 2:
            self.ui.resultLabel.setText("Result: Saldırmak için en az 2 asker gerekli.")
            self.update_action_panel()
            return

        attacker_name = self.display_territory_name(self.attacker_territory.name)
        defender_name = self.display_territory_name(self.defender_territory.name)

        chance_before_attack = self.estimate_conquest_chance(
            self.attacker_territory.armies,
            self.defender_territory.armies
        )

        # Güç farkı çok fazlaysa zar atmadan direkt ele geçirme.
        # Örnek: 10 asker, 2 askerli bölgeye saldırırsa 10 >= 2*3+1 olduğu için direkt alır.
        old_defender_armies = self.defender_territory.armies
        overpower_limit = old_defender_armies * 3 + 1

        if self.attacker_territory.armies >= overpower_limit:
            old_owner = self.defender_territory.owner

            old_owner.remove_territory(self.defender_territory)

            self.defender_territory.set_owner(current_player)
            current_player.add_territory(self.defender_territory)

            moving_armies = min(
                old_defender_armies + 1,
                self.attacker_territory.armies - 1
            )
            moving_armies = max(1, moving_armies)

            original_attacker_armies = self.attacker_territory.armies

            self.defender_territory.armies = moving_armies
            self.attacker_territory.remove_armies(moving_armies)

            self.ui.diceInfoLabel.setText(
                f"Overpower Attack\n"
                f"FROM: {attacker_name} ({original_attacker_armies})\n"
                f"TARGET: {defender_name} ({old_defender_armies})\n"
                f"Sonuç: Direkt ele geçirildi."
            )

            self.ui.resultLabel.setText(
                f"Result: {attacker_name} → {defender_name}\n"
                f"Güç üstünlüğüyle direkt ele geçirildi. "
                f"{moving_armies} asker aktarıldı."
            )

            self.attacker_territory = None
            self.defender_territory = None

            self.ui.attackerLabel.setText("FROM: None")
            self.ui.defenderLabel.setText("TARGET: None")

            winner = self.game.check_winner()

            if winner:
                self.ui.resultLabel.setText(f"🎉 {winner.name} kazandı!")
                self.ui.attackButton.setEnabled(False)
                self.ui.nextTurnButton.setEnabled(False)
                return

            self.update_screen()
            return

        attack_rolls, defend_rolls, attacker_losses, defender_losses = self.roll_risk_dice(
            self.attacker_territory.armies,
            self.defender_territory.armies
        )

        self.attacker_territory.remove_armies(attacker_losses)
        self.defender_territory.remove_armies(defender_losses)

        self.ui.diceInfoLabel.setText(
            f"Dice Roll\n"
            f"Attack: {attack_rolls}\n"
            f"Defense: {defend_rolls}\n"
            f"Chance: %{chance_before_attack}\n"
            f"Loss → A-{attacker_losses}, D-{defender_losses}"
        )

        result_message = (
            f"Result: {attacker_name} → {defender_name}\n"
            f"Zarlar: A{attack_rolls} / D{defend_rolls} | "
            f"Kayıp: Saldıran-{attacker_losses}, Savunan-{defender_losses}"
        )

        if self.defender_territory.armies == 0:
            old_owner = self.defender_territory.owner

            old_owner.remove_territory(self.defender_territory)

            self.defender_territory.set_owner(current_player)
            current_player.add_territory(self.defender_territory)

            moving_armies = min(3, self.attacker_territory.armies - 1)
            moving_armies = max(1, moving_armies)

            self.defender_territory.armies = moving_armies
            self.attacker_territory.remove_armies(moving_armies)

            result_message = (
                f"Result: {defender_name} ele geçirildi! "
                f"{moving_armies} asker {attacker_name} bölgesinden aktarıldı. "
                f"Saldırı öncesi ele geçirme ihtimali: %{chance_before_attack}."
            )

            self.attacker_territory = None
            self.defender_territory = None
            self.ui.attackerLabel.setText("FROM: None")
            self.ui.defenderLabel.setText("TARGET: None")

        else:
            if self.attacker_territory.armies < 2:
                result_message += "\n Saldıran bölgede yeterli asker kalmadı."
                self.attacker_territory = None
                self.defender_territory = None
                self.ui.attackerLabel.setText("FROM: None")
                self.ui.defenderLabel.setText("TARGET: None")

        self.ui.resultLabel.setText(result_message)

        winner = self.game.check_winner()

        if winner:
            self.ui.resultLabel.setText(f"🎉 {winner.name} kazandı!")
            self.ui.attackButton.setEnabled(False)
            self.ui.nextTurnButton.setEnabled(False)
            return

        self.update_screen()


game_window = RiskGameWindow


def run_app():
    app = QApplication(sys.argv)
    window = RiskGameWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()
