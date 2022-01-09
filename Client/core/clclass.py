import socket

class ClientConnect:
    def __inti__(self):
        self.scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Conn(self, ip, port):
        self.socket.connect((ip, port))
        self.ip = ip
        self.port = port
    
    def receive_data(self):
        self.dib = self.scoket.recv(1024)
        self.data = self.dib.decode("uft-8")
        return self.data

    def send_data(self, data):
        self.dib = bytes(data, "uft-8")
        self.socket.send(self.dib)

    def close(self):
        self.socket.close()