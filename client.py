import socket
import subprocess

REMOTE_HOST = '10.0.2.5'
REMOTE_PORT = 4444
PASSWORD = ""
escape = False
client = socket.socket()
print("Starting Connection")
client.connect((REMOTE_HOST, REMOTE_PORT)) 
input_password = input('Enter Password: ')
client.send(input_password.encode())
status = client.recv(1024).decode()
if status == "Incorrect Password...Closing Connection":
        client.close()
        escape = false

while !escape:
    command = input('Enter Command: ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    if output == "Disconnecting":
        client.close()
        escape = false
    print(f"Output: {output}")
