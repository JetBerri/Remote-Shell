from core.svclass import Server
from core.handleConnection import handleConnection

socket = Connection()
socket.Connection("127.0.0.1", 8080)

socket.Listen()
nconn, _ = socket.AllowConnection()

handleConnection(socket)

nconn.close()