import socket
import threading


HOST = "0.0.0.0"
PORT = 5555

clients = []
players = {}


def handle_client(client_socket, address):
    print(f"Yeni bağlantı: {address}")

    try:
        player_name = client_socket.recv(1024).decode("utf-8")

        if len(clients) >= 2:
            client_socket.send("SERVER_FULL".encode("utf-8"))
            client_socket.close()
            return

        clients.append(client_socket)

        player_number = len(clients)
        players[client_socket] = {
            "name": player_name,
            "role": f"Player {player_number}"
        }

        print(f"{player_name} oyuna bağlandı. Rol: Player {player_number}")
        print(f"Bağlı oyuncu sayısı: {len(clients)}")

        client_socket.send(f"CONNECTED|Player {player_number}".encode("utf-8"))

        if len(clients) == 2:
            broadcast("GAME_START|İki oyuncu bağlandı. Oyun başlıyor.")

        while True:
            message = client_socket.recv(1024).decode("utf-8")

            if not message:
                break

            print(f"{players[client_socket]['name']}: {message}")
            broadcast(f"MESSAGE|{players[client_socket]['name']}: {message}")

    except ConnectionResetError:
        print(f"{address} bağlantısı kesildi.")

    finally:
        if client_socket in clients:
            clients.remove(client_socket)

        if client_socket in players:
            print(f"{players[client_socket]['name']} oyundan ayrıldı.")
            del players[client_socket]

        client_socket.close()


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode("utf-8"))
        except:
            pass


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    print("Risk Game Server başlatıldı.")
    print(f"Server dinleniyor: {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        thread.start()


if __name__ == "__main__":
    start_server()