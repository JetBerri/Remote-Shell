# Installation
__Not tested in Windows and Termux__

Clone the repo:
```
git clone https://github.com/0xStevenson/Remote-Shell.git
```
Go to the directory:
```
cd Remote-Shell
```
Run setup:
```
sudo bash install.sh
```
Install requeriments:
```
pip install -r requeriments.txt
```

# Use

Run handleConnection.py (/Remote-Shell/Server/core/handleConnection.py) or:
```
sudo bash run.sh
```
Send the handleConnection but from /Client/core to the victim.

To make it available to work out of lan you'll have to edit the parts of the script that are using 127.0.0.1 as IP and port 8080 by default.

# Disclaimer

This tool has been made with educational purposes and I'm not responsable of any of your acts.
