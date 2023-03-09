import socket
import subprocess

REMOTE_HOST = '10.0.2.5'
REMOTE_PORT = 4444
IN_SHELL = False
PASSWORD = ""
client = socket.socket()
print("Starting Connection")
client.connect((REMOTE_HOST, REMOTE_PORT)) 
prompt = client.recv(1024)
prompt = prompt.decode()
print(f"{prompt}")
input_password = input('Enter Password: ')
client.send(input_password.encode())
print("Connected!")

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
