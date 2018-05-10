from requests.exceptions import ConnectionError
from socketIO_client_nexus import SocketIO, LoggingNamespace
import json

def connected():
    print('-[Request]> Connected with socket')

#Connects to socketio server
sio = SocketIO('192.168.2.9', 3000)

#socket requests
sio.on('connect', connected)

sio.on('rpiNotification', connected)

def changeView(roomID, view):
    print('-[request]> Send change view: ' + str(view))
    jsonData = json.dumps({'room': roomID, 'view': view})
    sio.emit('changeView', jsonData)

