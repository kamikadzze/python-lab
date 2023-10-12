import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

while True:
    message = input("Enter a sentence (type 'exit' to quit): ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'exit':
        break

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

client_socket.close()
