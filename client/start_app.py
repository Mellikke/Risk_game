import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_start_window import Ui_MainWindow
from config import SERVER_IP, SERVER_PORT
from network_client import NetworkClient
from waiting_app import WaitingWindow


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.network_client = None

        self.ui.connectButton.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        player_name = self.ui.playerNameInput.text().strip()

        if player_name == "":
            QMessageBox.warning(self, "Uyarı", "Lütfen oyuncu adınızı giriniz.")
            return

        try:
            self.network_client = NetworkClient(SERVER_IP, SERVER_PORT)
            response = self.network_client.connect(player_name)

            print("Bağlan butonuna basıldı.")
            print("Oyuncu adı:", player_name)
            print("Server IP:", SERVER_IP)
            print("Server Port:", SERVER_PORT)
            print("Server cevabı:", response)

            player_role = "Unknown"

            if response.startswith("CONNECTED|"):
                player_role = response.split("|")[1]

            self.waiting_window = WaitingWindow(player_name, player_role)
            self.waiting_window.show()
            self.close()

        except ConnectionRefusedError:
            QMessageBox.critical(
                self,
                "Bağlantı Hatası",
                "Server çalışmıyor olabilir. Önce server.py dosyasını çalıştırın."
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Hata",
                f"Bağlantı sırasında hata oluştu:\n{error}"
            )


def run_start_app():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_start_app()