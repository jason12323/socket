import socket
import time

a = input("room_NO?")

a = int(a)
a = ("127.0.0.1", a)
client = socket.socket()
try:
    client.connect(tuple(a))
except ConnectionRefusedError:
    print("can't connect to", tuple(a))
    exit()
print(client.recv(1024).decode())
nam = input("name?")
client.send(nam.encode())
for i in range(10):
    client.send(input("msg?").encode())
    print(client.recv(1024).decode())
client.close()