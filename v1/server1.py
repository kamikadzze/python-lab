import socket
import datetime

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345  # Use any available port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen(1)
print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

data = client_socket.recv(1024).decode('utf-8')
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Received: '{data}' at {current_time}")

client_socket.close()
server_socket.close()
