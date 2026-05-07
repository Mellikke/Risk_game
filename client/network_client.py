import socket


class NetworkClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None
        self.buffer = ""

    def connect(self, player_name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))

        self.client_socket.sendall((player_name + "\n").encode("utf-8"))

        response = self.receive_message()
        return response

    def send_message(self, message):
        if self.client_socket:
            self.client_socket.sendall((message + "\n").encode("utf-8"))

    def receive_message(self):
        while "\n" not in self.buffer:
            data = self.client_socket.recv(4096).decode("utf-8")

            if not data:
                return None

            self.buffer += data

        message, self.buffer = self.buffer.split("\n", 1)
        return message.strip()

    def close(self):
        if self.client_socket:
            self.client_socket.close()