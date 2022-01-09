from core.clclass import ClientConnect
from core.handleConnection import handleConnection

socket = ClientConnect()
socket.connect("127.0.0.1", 8080)

handleConnection(socket)

socket.close()

