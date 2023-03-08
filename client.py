import socket
import subprocess

REMOTE_HOST = '10.0.2.5'
REMOTE_PORT = 4444
IN_SHELL = False
PASSWORD = ""
client = socket.socket()
print("Starting Connection")
input_password = input('Enter Password: ')
if input_password == PASSWORD:
    IN_SHELL = True
    client.connect((REMOTE_HOST, REMOTE_PORT)) 
    print("Connected!")
else:
    print("Incorrect Password")

while IN_SHELL == True:
    command = input('Enter Command: ')
    if command == "exit":
        IN_SHELL = False
        break;
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
