import socket
import subprocess

REMOTE_HOST = '10.0.2.5'
REMOTE_PORT = 4444
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print("Output: {output}")
