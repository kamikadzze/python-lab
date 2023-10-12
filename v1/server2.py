import socket
import datetime
import threading
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def handle_client(client_socket, address):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Received from {address}: '{data}' at {current_time}")

            time.sleep(5)

            response = f"Server received: '{data}'"
            client_socket.send(response.encode('utf-8'))
    except ConnectionAbortedError:
        print(f"Connection aborted by {address}")
    finally:
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)
print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
