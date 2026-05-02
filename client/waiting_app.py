import sys
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal

from ui_waiting_window import Ui_MainWindow
from app import RiskGameWindow


class WaitingWindow(QMainWindow):
    server_message_signal = pyqtSignal(str)

    def __init__(self, player_name="Test Oyuncu", player_role="Player 1", network_client=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player_name = player_name
        self.player_role = player_role
        self.network_client = network_client

        self.ui.playerInfoLabel.setText(f"Oyuncu: {player_name} ({player_role})")
        self.ui.statusLabel.setText("Rakip oyuncunun bağlanması bekleniyor...")

        self.server_message_signal.connect(self.handle_server_message)

        if self.network_client is not None:
            self.listen_thread = threading.Thread(target=self.listen_server)
            self.listen_thread.daemon = True
            self.listen_thread.start()

    def listen_server(self):
        while True:
            try:
                message = self.network_client.client_socket.recv(1024).decode("utf-8")

                if not message:
                    break

                self.server_message_signal.emit(message)

            except:
                break

    def handle_server_message(self, message):
        print("Server mesajı:", message)

        if message.startswith("GAME_START"):
            self.ui.statusLabel.setText("İki oyuncu bağlandı. Oyun başlıyor...")

            self.game_window = RiskGameWindow(
                player_name=self.player_name,
                player_role=self.player_role,
                network_client=self.network_client
            )

            self.game_window.show()
            self.close()


def run_waiting_app():
    app = QApplication(sys.argv)
    window = WaitingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_waiting_app()