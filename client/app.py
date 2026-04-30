import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget
from game.game_engine import GameEngine


class RiskGameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.game = GameEngine()
        self.game.setup_game()

        self.setWindowTitle("Risk Game")
        self.setGeometry(200, 200, 600, 500)

        self.title_label = QLabel("Risk Game")
        self.current_player_label = QLabel()
        self.territory_list = QListWidget()
        self.attacker_label = QLabel("Attacker: None")
        self.defender_label = QLabel("Defender: None")
        self.result_label = QLabel("Result: Henüz saldırı yapılmadı")
        self.next_turn_button = QPushButton("Next Turn")
        self.reinforcement_label = QLabel("Reinforcements: 0")
        self.phase_label = QLabel("Phase: Reinforcement")
        self.attack_button = QPushButton("Attack")


        self.selected_territory = None
        self.attacker_territory = None
        self.defender_territory = None
        self.phase = "reinforcement"


        self.next_turn_button.clicked.connect(self.next_turn)
        self.territory_list.itemClicked.connect(self.select_territory)
        self.attack_button.clicked.connect(self.attack)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.current_player_label)
        layout.addWidget(self.reinforcement_label)
        layout.addWidget(self.phase_label)
        layout.addWidget(self.attacker_label)
        layout.addWidget(self.defender_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.territory_list)
        layout.addWidget(self.next_turn_button)
        layout.addWidget(self.attack_button)

        self.setLayout(layout)

        self.update_screen()

    def update_screen(self):
        current_player = self.game.get_current_player()
        self.reinforcement_label.setText(
            f"Reinforcements: {current_player.reinforcements}"
        )
        self.current_player_label.setText(f"Current Player: {current_player.name}")

        self.territory_list.clear()

        self.phase_label.setText(f"Phase: {self.phase}")
        for territory in self.game.game_map.territories.values():
            self.territory_list.addItem(
                f"{territory.name} | Owner: {territory.owner.name} | Armies: {territory.armies}"
            )

    def next_turn(self):
        self.game.next_turn()
        self.game.start_turn()

        self.phase = "reinforcement"

        self.attacker_territory = None
        self.defender_territory = None
        self.attacker_label.setText("Attacker: None")
        self.defender_label.setText("Defender: None")
        self.result_label.setText("Result: Yeni tur başladı, asker yerleştir")

        self.update_screen()

    def select_territory(self, item):
        text = item.text()
        territory_name = text.split(" | ")[0]
        selected = self.game.game_map.get_territory(territory_name)

        current_player = self.game.get_current_player()

        if self.phase == "reinforcement":
            if selected.owner != current_player:
                self.result_label.setText("Result: Sadece kendi bölgene asker koyabilirsin")
                return

            if current_player.reinforcements > 0:
                selected.add_armies(1)
                current_player.reinforcements -= 1
                self.result_label.setText(f"Result: {selected.name} bölgesine 1 asker eklendi")

                if current_player.reinforcements == 0:
                    self.phase = "attack"
                    self.result_label.setText("Result: Takviye bitti, saldırı aşamasına geçildi")

                self.update_screen()
                return

        if self.phase == "attack":
            if selected.owner == current_player:
                self.attacker_territory = selected
                self.attacker_label.setText(f"Attacker: {selected.name}")
            else:
                self.defender_territory = selected
                self.defender_label.setText(f"Defender: {selected.name}")

    def attack(self):
        if self.phase != "attack":
            self.result_label.setText("Result: Önce takviye askerlerini yerleştirmelisin")
            return

        if self.attacker_territory is None or self.defender_territory is None:
            self.result_label.setText("Result: Önce attacker ve defender seç")
            return

        if self.defender_territory not in self.attacker_territory.neighbors:
            self.result_label.setText("Result: Sadece komşu bölgelere saldırabilirsin")
            return

        if self.attacker_territory.owner != self.game.get_current_player():
            self.result_label.setText("Result: Sadece kendi bölgenle saldırabilirsin")
            return

        if self.attacker_territory.owner == self.defender_territory.owner:
            self.result_label.setText("Result: Kendi bölgene saldıramazsın")
            return

        if self.attacker_territory.armies < 2:
            self.result_label.setText("Result: Saldırmak için en az 2 asker gerekli")
            return

        attack_roll = random.randint(1, 6)
        defend_roll = random.randint(1, 6)

        if attack_roll > defend_roll:
            self.defender_territory.remove_armies(1)
            self.result_label.setText(
                f"Result: Saldıran zar {attack_roll}, Savunan zar {defend_roll} → Savunan 1 asker kaybetti"
            )

            if self.defender_territory.armies == 0:
                old_owner = self.defender_territory.owner
                old_owner.remove_territory(self.defender_territory)

                self.defender_territory.set_owner(self.attacker_territory.owner)
                self.attacker_territory.owner.add_territory(self.defender_territory)

                self.defender_territory.armies = 1
                self.attacker_territory.remove_armies(1)

                self.result_label.setText(
                    f"Result: {self.defender_territory.name} ele geçirildi!"
                )
        else:
            self.attacker_territory.remove_armies(1)
            self.result_label.setText(
                f"Result: Saldıran zar {attack_roll}, Savunan zar {defend_roll} → Saldıran 1 asker kaybetti"
            )

        self.attacker_territory = None
        self.defender_territory = None
        self.attacker_label.setText("Attacker: None")
        self.defender_label.setText("Defender: None")


        winner = self.game.check_winner()
        if winner:
            self.result_label.setText(f"🎉 {winner.name} kazandı!")
            self.attack_button.setEnabled(False)
            self.next_turn_button.setEnabled(False)
            return

        self.update_screen()

def run_app():
    app = QApplication(sys.argv)
    window = RiskGameWindow()
    window.show()
    sys.exit(app.exec())