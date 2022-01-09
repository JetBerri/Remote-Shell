from colorama import Fore

def run_command(socket):
    print(Fore.GREEN + "[+] Running commands")

    while True:

        command = input(">$  ")

        socket.send_data(command)

        if command == "stop":
            break
        
        result = socket.receive_data()

        print(result)