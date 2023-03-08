import socket

HOST = "10.0.2.5"
PORT = 4444
server = socket.socket()
server.bind((HOST, PORT))
print("Server Started)
print("Listening for connections")
server.listen(1)
client, client_addr = server.accept()
print("Client connected to the server")

while True:
    command = input("Enter Command: ")
    command = command.encode()
    client.send(command)
    print("[+] Command sent")
    output = client.recv(1024)
    output = output.decode()
    print("Output: {output}")
