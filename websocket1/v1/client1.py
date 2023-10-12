import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

message = input("Enter a sentence: ")
client_socket.send(message.encode('utf-8'))

client_socket.close()
