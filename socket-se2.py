import socketserver
import socket
import random
msgs = [b"None"]
class serverc(socketserver.BaseRequestHandler):
    nam = ""
    def handle(self):
        global msgs
        conn = self.request
        conn: socket.socket
        conn.send(b"Start!")
        name = conn.recv(1024)
        self.nam = name.decode()
        if name == b"":
            return
        print(name.decode(), "join!")
        while True:
            data = conn.recv(1024)
            conn.send(msgs[-1])
            if data != b"":
                msgs.append(name+":".encode()+data)
                print(name.decode()+":"+data.decode())
    def finish(self):
        print(self.nam+" quit!")


po = random.randint(20000, 50000)
print("connect at", po)
server = socketserver.ThreadingTCPServer(("127.0.0.1", po), serverc)
server.serve_forever()