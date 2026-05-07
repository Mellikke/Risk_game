import sys
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal

from ui_waiting_window import Ui_MainWindow
from app import game_window


class WaitingWindow(QMainWindow):
    server_message_signal = pyqtSignal(str)

    def __init__(self, player_name="Test Oyuncu", player_role="Player 1", network_client=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player_name = player_name
        self.player_role = player_role
        self.network_client = network_client

        self.game_window = None
        self.running = True

        self.ui.player_info_layer.setText(
            f"Oyuncu: {player_name} ({player_role})"
        )
        self.ui.statusLabel.setText("Rakip oyuncunun bağlanması bekleniyor...")

        self.server_message_signal.connect(self.handle_server_message)

        if self.network_client is not None:
            self.listen_thread = threading.Thread(
                target=self.listen_server,
                daemon=True
            )
            self.listen_thread.start()

    def listen_server(self):
        while self.running:
            try:
                # ÖNEMLİ:
                # Direkt recv() kullanmıyoruz.
                # Çünkü network_client mesajları \n ile satır satır ayırıyor.
                message = self.network_client.receive_message()

                if not message:
                    break

                self.server_message_signal.emit(message)

            except Exception as error:
                print("Waiting server dinleme hatası:", error)
                break

    def handle_server_message(self, message):
        print("WaitingWindow server mesajı:", message)

        if message.startswith("GAME_START|"):
            self.ui.statusLabel.setText("İki oyuncu bağlandı. Oyun başlıyor...")

            self.game_window = game_window(
                player_name=self.player_name,
                player_role=self.player_role,
                network_client=self.network_client
            )

            self.game_window.show()
            self.close()
            return

        # Eğer GAME_STATE mesajı oyun penceresi açıldıktan sonra yanlışlıkla buraya gelirse,
        # mesajı oyun penceresine aktar.
        if message.startswith("GAME_STATE|"):
            if self.game_window is not None:
                self.game_window.process_server_message(message)
            return

        if message.startswith("ERROR|"):
            error_text = message.split("|", 1)[1]
            self.ui.statusLabel.setText(error_text)
            return

        if message == "SERVER_FULL":
            self.ui.statusLabel.setText("Server dolu. Oyuna bağlanılamadı.")
            return

    def closeEvent(self, event):
        self.running = False
        super().closeEvent(event)


def run_waiting_app():
    app = QApplication(sys.argv)
    window = WaitingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_waiting_app()