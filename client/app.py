import sys
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_game_window import Ui_MainWindow
from game.game_engine import GameEngine


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
        self.phase = "reinforcement"

        self.ui.nextTurnButton.clicked.connect(self.next_turn)
        self.ui.attackButton.clicked.connect(self.attack)
        self.ui.territoryList.itemClicked.connect(self.select_territory_from_list)

        self.connect_map_controls()
        self.update_screen()

    def connect_map_controls(self):
        """
        Harita seçimlerini bağlar.
        Öncelik yeni WorldMapWidget'tadır.
        Gizli butonlar sadece eski 6 bölgeyle uyumluluk için bağlı kalır.
        """

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
                f"{display_name}  |  {owner_short}  |  {territory.armies} asker"
            )

            self.update_hidden_button(territory)
            self.update_world_map_territory(territory)

        if hasattr(self.ui, "worldMapWidget"):
            self.ui.worldMapWidget.update()

    def update_world_map_territory(self, territory):
        if not hasattr(self.ui, "worldMapWidget"):
            return

        display_name = self.display_territory_name(territory.name)

        for item in self.ui.worldMapWidget.territories:
            if item["name"] == display_name or item["name"] == territory.name:
                item["owner"] = territory.owner.name
                item["armies"] = territory.armies

                if territory.owner.name == "Player 1":
                    item["color"] = item["color"].fromString("#d32929")
                else:
                    item["color"] = item["color"].fromString("#2f63e6")

                break

    def update_hidden_button(self, territory):
        """
        Eski app.py mantığında kullanılan gizli QPushButton'ları güncel tutar.
        Yeni harita görünümü bunları göstermez.
        """

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
        self.game.next_turn()
        self.game.start_turn()

        self.phase = "reinforcement"

        self.attacker_territory = None
        self.defender_territory = None

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
            f"Result: {selected.name} bölgesine 1 asker eklendi."
        )

        if current_player.reinforcements == 0:
            self.phase = "attack"
            self.ui.resultLabel.setText(
                "Result: Takviye bitti, saldırı aşamasına geçildi."
            )

        self.update_screen()

    def handle_attack_selection(self, selected, current_player):
        if selected.owner == current_player:
            self.attacker_territory = selected
            self.defender_territory = None

            self.ui.attackerLabel.setText(f"FROM: {selected.name}")
            self.ui.defenderLabel.setText("TARGET: None")
            self.ui.resultLabel.setText(
                f"Result: Saldıran bölge seçildi: {selected.name}"
            )
            return

        if self.attacker_territory is None:
            self.ui.resultLabel.setText(
                "Result: Önce kendi bölgelerinden bir saldıran bölge seçmelisin."
            )
            return

        self.defender_territory = selected

        self.ui.defenderLabel.setText(f"TARGET: {selected.name}")
        self.ui.resultLabel.setText(
            f"Result: Hedef bölge seçildi: {selected.name}"
        )

    def attack(self):
        if self.phase != "attack":
            self.ui.resultLabel.setText("Result: Önce takviye askerlerini yerleştirmelisin.")
            return

        if self.attacker_territory is None or self.defender_territory is None:
            self.ui.resultLabel.setText("Result: Önce FROM ve TARGET seç.")
            return

        if self.defender_territory not in self.attacker_territory.neighbors:
            self.ui.resultLabel.setText(
                f"Result: {self.attacker_territory.name} ile "
                f"{self.defender_territory.name} komşu değil."
            )
            return

        if self.attacker_territory.owner != self.game.get_current_player():
            self.ui.resultLabel.setText("Result: Sadece kendi bölgenle saldırabilirsin.")
            return

        if self.attacker_territory.owner == self.defender_territory.owner:
            self.ui.resultLabel.setText("Result: Kendi bölgene saldıramazsın.")
            return

        if self.attacker_territory.armies < 2:
            self.ui.resultLabel.setText("Result: Saldırmak için en az 2 asker gerekli.")
            return

        attack_roll = random.randint(1, 6)
        defend_roll = random.randint(1, 6)

        if attack_roll > defend_roll:
            self.defender_territory.remove_armies(1)

            self.ui.resultLabel.setText(
                f"Result: Saldıran zar {attack_roll}, savunan zar {defend_roll}. "
                f"Savunan 1 asker kaybetti."
            )

            if self.defender_territory.armies == 0:
                old_owner = self.defender_territory.owner
                old_owner.remove_territory(self.defender_territory)

                self.defender_territory.set_owner(self.attacker_territory.owner)
                self.attacker_territory.owner.add_territory(self.defender_territory)

                self.defender_territory.armies = 1
                self.attacker_territory.remove_armies(1)

                self.ui.resultLabel.setText(
                    f"Result: {self.defender_territory.name} ele geçirildi!"
                )
        else:
            self.attacker_territory.remove_armies(1)

            self.ui.resultLabel.setText(
                f"Result: Saldıran zar {attack_roll}, savunan zar {defend_roll}. "
                f"Saldıran 1 asker kaybetti."
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


# Eski importlar bozulmasın diye alias bırakıyoruz.
game_window = RiskGameWindow


def run_app():
    app = QApplication(sys.argv)
    window = RiskGameWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()