import socket
import threading
import os
import sys
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from game.game_engine import GameEngine


HOST = "0.0.0.0"
PORT = 5555

clients = []
players = {}

game = GameEngine()
game.setup_game()

phase = "reinforcement"
fortify_done = False
game_over = False

lock = threading.Lock()


def send_to_client(client_socket, message):
    try:
        client_socket.sendall((message + "\n").encode("utf-8"))
    except Exception:
        pass


def broadcast(message):
    disconnected_clients = []

    for client in clients[:]:
        try:
            client.sendall((message + "\n").encode("utf-8"))
        except Exception:
            disconnected_clients.append(client)

    for client in disconnected_clients:
        remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

    if client_socket in players:
        print(f"{players[client_socket]['name']} oyundan ayrıldı.")
        del players[client_socket]

    try:
        client_socket.close()
    except Exception:
        pass

def serialize_game_state():
    current_player = game.get_current_player()

    territory_parts = []

    for territory in game.game_map.territories.values():
        owner_name = territory.owner.name if territory.owner else "None"
        territory_parts.append(
            f"{territory.name},{owner_name},{territory.armies}"
        )

    territories_text = ";".join(territory_parts)

    return (
        f"GAME_STATE|"
        f"current_player={current_player.name}|"
        f"phase={phase}|"
        f"reinforcements={current_player.reinforcements}|"
        f"territories={territories_text}"
    )


def send_game_state_to_all():
    broadcast(serialize_game_state())


def roll_risk_dice(attacker_armies, defender_armies):
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


def check_turn(client_socket):
    if client_socket not in players:
        send_to_client(client_socket, "ERROR|Oyuncu bulunamadı.")
        return False

    player_role = players[client_socket]["role"]
    current_player = game.get_current_player()

    if player_role != current_player.name:
        send_to_client(client_socket, "ERROR|Sıra sende değil.")
        return False

    return True


def handle_place_army(client_socket, territory_name):
    global phase

    if game_over:
        send_to_client(client_socket, "ERROR|Oyun bitti.")
        send_game_state_to_all()
        return

    if not check_turn(client_socket):
        send_game_state_to_all()
        return

    current_player = game.get_current_player()

    if phase != "reinforcement":
        send_game_state_to_all()
        send_to_client(client_socket, "ERROR|Şu anda konumlandırma aşamasında değilsin.")
        return

    territory = game.game_map.get_territory(territory_name)

    if territory is None:
        send_game_state_to_all()
        send_to_client(client_socket, "ERROR|Bölge bulunamadı.")
        return

    if territory.owner != current_player:
        send_game_state_to_all()
        send_to_client(client_socket, "ERROR|Sadece kendi bölgene asker koyabilirsin.")
        return

    if current_player.reinforcements <= 0:
        phase = "attack"
        send_game_state_to_all()
        broadcast("RESULT|Konumlandırma tamamlandı. Savaş aşamasına geçildi.")
        return

    territory.add_armies(1)
    current_player.reinforcements -= 1

    if current_player.reinforcements <= 0:
        current_player.reinforcements = 0
        phase = "attack"
        send_game_state_to_all()
        broadcast("RESULT|Konumlandırma tamamlandı. Savaş aşamasına geçildi.")
        return

    send_game_state_to_all()
    send_to_client(
        client_socket,
        f"RESULT|{territory.name} bölgesine 1 asker yerleştirildi. "
        f"Kalan asker: {current_player.reinforcements}"
    )
def handle_next_phase(client_socket):
    global phase, fortify_done

    if game_over:
        send_to_client(client_socket, "ERROR|Oyun bitti.")
        return

    if not check_turn(client_socket):
        return

    current_player = game.get_current_player()

    if phase == "reinforcement":
        if current_player.reinforcements > 0:
            send_to_client(
                client_socket,
                f"ERROR|Konumlandırma zorunlu. Kalan asker: {current_player.reinforcements}"
            )
            return

        phase = "attack"
        send_game_state_to_all()
        broadcast("RESULT|Savaş aşamasına geçildi.")
        return

    if phase == "attack":
        phase = "fortify"
        fortify_done = False
        send_game_state_to_all()
        broadcast(
            "RESULT|Takviye / asker aktarma aşamasına geçildi. "
            "İstersen kendi komşu bölgelerin arasında asker aktarabilirsin."
        )
        return

    if phase == "fortify":
        game.next_turn()
        game.start_turn()

        phase = "reinforcement"
        fortify_done = False

        current_player = game.get_current_player()

        send_game_state_to_all()
        broadcast(
            f"RESULT|Tur bitti. Sıra {current_player.name} oyuncusunda. "
            "Konumlandırma aşaması başladı."
        )
        return


def handle_attack(client_socket, attacker_name, defender_name):
    global game_over

    if game_over:
        send_to_client(client_socket, "ERROR|Oyun bitti.")
        return

    if not check_turn(client_socket):
        return

    current_player = game.get_current_player()

    if phase != "attack":
        send_to_client(client_socket, "ERROR|Şu anda savaş aşamasında değilsin.")
        return

    attacker = game.game_map.get_territory(attacker_name)
    defender = game.game_map.get_territory(defender_name)

    if attacker is None or defender is None:
        send_to_client(client_socket, "ERROR|Saldırı bölgesi bulunamadı.")
        return

    if attacker.owner != current_player:
        send_to_client(client_socket, "ERROR|Sadece kendi bölgenle saldırabilirsin.")
        return

    if defender.owner == current_player:
        send_to_client(client_socket, "ERROR|Kendi bölgene saldıramazsın.")
        return

    if defender not in attacker.neighbors:
        send_to_client(client_socket, "ERROR|Bu iki bölge komşu değil.")
        return

    if attacker.armies < 2:
        send_to_client(client_socket, "ERROR|Saldırmak için en az 2 asker gerekli.")
        return

    # Güç üstünlüğü kuralı:
    # Örn: 10 asker, 2 askerlik yere saldırıyorsa direkt ele geçirir.
    overpower_limit = defender.armies * 3 + 1

    if attacker.armies >= overpower_limit:
        old_owner = defender.owner
        old_defender_armies = defender.armies

        if old_owner:
            old_owner.remove_territory(defender)

        defender.set_owner(current_player)
        current_player.add_territory(defender)

        # Kaynak bölgede en az 1 asker kalmalı.
        moving_armies = min(old_defender_armies + 1, attacker.armies - 1)
        moving_armies = max(1, moving_armies)

        defender.armies = moving_armies
        attacker.remove_armies(moving_armies)

        winner = game.check_winner()

        send_game_state_to_all()

        if winner:
            game_over = True
            broadcast(f"RESULT|🎉 {winner.name} oyunu kazandı!")
        else:
            broadcast(
                f"RESULT|Güç üstünlüğü! {attacker.name} → {defender.name} "
                f"zar atmadan ele geçirildi. {moving_armies} asker aktarıldı."
            )

        return

    # Güç üstünlüğü yoksa normal zar sistemi çalışır.
    attack_rolls, defend_rolls, attacker_losses, defender_losses = roll_risk_dice(
        attacker.armies,
        defender.armies
    )

    attacker.remove_armies(attacker_losses)
    defender.remove_armies(defender_losses)

    result_message = (
        f"RESULT|Saldırı: {attacker.name} → {defender.name} | "
        f"Zarlar A{attack_rolls} / D{defend_rolls} | "
        f"Kayıp: Saldıran-{attacker_losses}, Savunan-{defender_losses}"
    )

    if defender.armies <= 0:
        old_owner = defender.owner

        if old_owner:
            old_owner.remove_territory(defender)

        defender.set_owner(current_player)
        current_player.add_territory(defender)

        moving_armies = min(3, attacker.armies - 1)
        moving_armies = max(1, moving_armies)

        defender.armies = moving_armies
        attacker.remove_armies(moving_armies)

        result_message = (
            f"RESULT|{defender.name} ele geçirildi! "
            f"{moving_armies} asker {attacker.name} bölgesinden aktarıldı."
        )

    winner = game.check_winner()

    if winner:
        game_over = True
        send_game_state_to_all()
        broadcast(f"RESULT|🎉 {winner.name} oyunu kazandı!")
        return

    send_game_state_to_all()
    broadcast(result_message)

def handle_fortify(client_socket, from_name, to_name, amount_text):
    global fortify_done

    if game_over:
        send_to_client(client_socket, "ERROR|Oyun bitti.")
        return

    if not check_turn(client_socket):
        return

    current_player = game.get_current_player()

    if phase != "fortify":
        send_to_client(client_socket, "ERROR|Şu anda asker aktarım aşamasında değilsin.")
        return

    if fortify_done:
        send_to_client(client_socket, "ERROR|Bu turda asker aktarımı zaten yapıldı.")
        return

    try:
        amount = int(amount_text)
    except ValueError:
        send_to_client(client_socket, "ERROR|Aktarılacak asker sayısı geçersiz.")
        return

    if amount <= 0:
        send_to_client(client_socket, "ERROR|Aktarılacak asker sayısı 1 veya daha fazla olmalı.")
        return

    from_territory = game.game_map.get_territory(from_name)
    to_territory = game.game_map.get_territory(to_name)

    if from_territory is None or to_territory is None:
        send_to_client(client_socket, "ERROR|Bölge bulunamadı.")
        return

    if from_territory.owner != current_player or to_territory.owner != current_player:
        send_to_client(client_socket, "ERROR|Sadece kendi bölgelerin arasında asker aktarabilirsin.")
        return

    if to_territory not in from_territory.neighbors:
        send_to_client(client_socket, "ERROR|Asker aktarımı için bölgeler komşu olmalı.")
        return

    if from_territory.armies - amount < 1:
        send_to_client(
            client_socket,
            "ERROR|Kaynak bölgede en az 1 asker kalmalı."
        )
        return

    from_territory.remove_armies(amount)
    to_territory.add_armies(amount)

    fortify_done = True

    send_game_state_to_all()
    broadcast(
        f"RESULT|{amount} asker {from_territory.name} bölgesinden "
        f"{to_territory.name} bölgesine aktarıldı."
    )


def handle_client_message(client_socket, message):
    with lock:
        if client_socket not in players:
            return

        if message.startswith("PLACE_ARMY|"):
            territory_name = message.split("|", 1)[1].strip()
            handle_place_army(client_socket, territory_name)
            return

        if message == "NEXT_PHASE":
            handle_next_phase(client_socket)
            return

        if message.startswith("ATTACK|"):
            try:
                _, attacker_name, defender_name = message.split("|", 2)
                handle_attack(
                    client_socket,
                    attacker_name.strip(),
                    defender_name.strip()
                )
            except ValueError:
                send_to_client(client_socket, "ERROR|Saldırı komutu hatalı.")
            return

        if message.startswith("FORTIFY|"):
            try:
                _, from_name, to_name, amount_text = message.split("|", 3)
                handle_fortify(
                    client_socket,
                    from_name.strip(),
                    to_name.strip(),
                    amount_text.strip()
                )
            except ValueError:
                send_to_client(client_socket, "ERROR|Asker aktarım komutu hatalı.")
            return

        player_name = players[client_socket]["name"]
        broadcast(f"MESSAGE|{player_name}: {message}")


def handle_client(client_socket, address):
    print(f"Yeni bağlantı: {address}")

    file_reader = None

    try:
        file_reader = client_socket.makefile("r", encoding="utf-8", newline="\n")

        player_name = file_reader.readline().strip()

        if not player_name:
            client_socket.close()
            return

        with lock:
            if len(clients) >= 2:
                send_to_client(client_socket, "SERVER_FULL")
                client_socket.close()
                return
            clients.append(client_socket)

            player_number = len(clients)
            player_role = f"Player {player_number}"

            players[client_socket] = {
                "name": player_name,
                "role": player_role
            }

        print(f"{player_name} oyuna bağlandı. Rol: {player_role}")
        print(f"Bağlı oyuncu sayısı: {len(clients)}")

        send_to_client(client_socket, f"CONNECTED|{player_role}")

        if len(clients) == 2:
            broadcast("GAME_START|İki oyuncu bağlandı. Oyun başlıyor.")
            send_game_state_to_all()

        while True:
            message = file_reader.readline()

            if not message:
                break

            message = message.strip()

            if not message:
                continue

            if client_socket not in players:
                break

            print(f"{players[client_socket]['name']}: {message}")
            handle_client_message(client_socket, message)

    except ConnectionResetError:
        print(f"{address} bağlantısı kesildi.")

    except Exception as error:
        print(f"Server client hatası: {error}")

    finally:
        with lock:
            if client_socket in clients:
                clients.remove(client_socket)

            if client_socket in players:
                print(f"{players[client_socket]['name']} oyundan ayrıldı.")
                del players[client_socket]

        try:
            if file_reader:
                file_reader.close()
        except Exception:
            pass

        try:
            client_socket.close()
        except Exception:
            pass


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    print("Risk Game Server başlatıldı.")
    print(f"Server dinleniyor: {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True
        )
        thread.start()


if __name__ == "__main__":
    start_server()