from requests.exceptions import ConnectionError
from socketIO_client_nexus import SocketIO, LoggingNamespace
import json
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import configHandler as config

def on_connect():
    print('-[Request]> Connected with socket')

#Connects to socketio server
sio = SocketIO(config.getData('app_data', 'socket_url'), config.getData('app_data', 'socket_port', 'int')) 

#socket requests


def changeView(roomID, view):
    print('-[request]> Send change view: ' + str(view))
    jsonData = json.dumps({'room': roomID, 'view': view})
    sio.emit('changeView', jsonData)

def verifyUser(roomID, card):
    print('-[request]> Send change view: ' + str(card))
    jsonData = json.dumps({'room': roomID, 'card': card})
    sio.emit('verifyUser', jsonData)
    

def checkConnection():
    sio.on('connect', on_connect)
    sio.on('rpiNotification', on_connect)
