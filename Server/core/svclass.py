import socket
from colorama import Fore

# use it if needed

size = 4*1024

class Server:
    def __init__(self):
        # tcp
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

             #change ip and port nuber
    def Connection(self, ip="127.0.0.1", port=8080):
         self.ip = ip
         self.port = port
         self.adress = (self.ip, self.port)
         self.socket.bind(self.adress)
    
    def Listen(self, backlog = 5):
        self.socket.listen(backlog)

    def AllowConnection(self):
        self.client_connection, self.client_address = self.socket.accept()
        print(Fore.GREEN + "[+] Connection established.")
        return(self.client_connection, self.client_address)
    
    def send_data(self, usr_input):
        usr_input_b = byte(usr_input, "uft-8")
        self.client_conn.send(user_input_bytes)

    def rdata(self):

        rdb = self.client_connection.recv(size)
        self.data = rdb.decode("uft-8")
        return self.data