from socketIO_client_nexus import SocketIO, LoggingNamespace
import json

def connected():
    print('-[Request]> Connected with socket')

def on_retrieveNotification(*args):
    print('got it: ', args)
    
#Connects to socketio server
sio = SocketIO('192.168.2.9', 3000, LoggingNamespace)

#socket requests
sio.on('connect', connected())
sio.on('rpiNotifcation', on_retrieveNotification())

def changeView(roomID, view):
    print('-[request]> Send change view: ' + str(view))
    jsonData = json.dumps({'room': roomID, 'view': view})
    sio.emit('changeView', jsonData)

    
