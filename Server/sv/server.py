# modules

import socket
import os
import datetime
from colorama import Fore
import time
#import class

# socket ip and port working (local)
# for out of lan attacks change the ip and port

ip = "127.0.0.1"
port = 8080

# connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(2)

    print(Fore.MAGENTA + "\nThis tool has been coded by 0xStevenson")
    print(Fore.MAGENTA + "\nI'm not responsable of your acts, this tool has been made with educational purposes.")

    print(Fore.WHITE + "\nConnection started at " + str(datetime.datetime.now()))
    print( Fore.GREEN + "\n[-] Waiting for connection...")
    client_s, client_add = s.accept()
    print( Fore.GREEN + "\n[+] Established connection...")

    msg = "working" # custom msg that will be printed in client shell

    client_s.send(msg.encode())

    client_s.close()

    s.close()

except KeyboardInterrupt:
    print(Fore.RED + "You pressed Ctrl+ C, exiting....")
    time.sleep(3)
    exit()

finally:
    print(Fore.GREEN + "Thanks for using!")