from requests.exceptions import ConnectionError
from socketIO_client_nexus import SocketIO, LoggingNamespace
import json

def on_connect():
    print('-[Request]> Connected with socket')

#Connects to socketio server
sio = SocketIO('192.168.43.194', 3000) 

#socket requests


def changeView(roomID, view):
    print('-[request]> Send change view: ' + str(view))
    jsonData = json.dumps({'room': roomID, 'view': view})
    sio.emit('changeView', jsonData)

def checkConnection():
    sio.on('connect', on_connect)
    sio.on('rpiNotification', on_connect)
