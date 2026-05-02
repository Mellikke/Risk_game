import socket


class NetworkClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None

    def connect(self, player_name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))

        self.client_socket.send(player_name.encode("utf-8"))

        response = self.client_socket.recv(1024).decode("utf-8")
        return response

    def send_message(self, message):
        if self.client_socket:
            self.client_socket.send(message.encode("utf-8"))

    def close(self):
        if self.client_socket:
            self.client_socket.close()