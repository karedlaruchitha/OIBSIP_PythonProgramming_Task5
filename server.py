import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    print("Server started...")
    while True:
        client, address = server.accept()
        print(f"Connected: {address}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()