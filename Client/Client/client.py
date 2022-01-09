import socket
import subprocess

size = 1024

# for out of lan attacks change the ip and port

ip = "127.0.0.1"
port = 8080

# socket connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adress = (ip, port) # needed for socket (documentation)
s.connect(adress)

msg_recvd = s.recv(size)

print(msg_recvd.decode())
s.close()