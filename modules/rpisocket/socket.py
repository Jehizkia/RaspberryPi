from socketIO_client_nexus import SocketIO, LoggingNamespace
import json

def connected():
    print('-> Connected with socket')

#Connects to socketio server
sio = SocketIO('192.168.2.9', 3000, LoggingNamespace)

sio.on('connect', connected())
def changeView(roomID, view):
    print('send to server: ' + str(view))
    jsonData = json.dumps({'room': roomID, 'view': view})
    sio.emit('changeView', jsonData)

    
