import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.1.109'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('\nChoose Mathematical Function, [L]-Logarithmic [S]-Square Root [E]-Exponential: ')

    if Input == 'L' or Input == 'S' or Input == 'E':
        num = input("Enter any number: ")
        Input = Input + ":" + num
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()
