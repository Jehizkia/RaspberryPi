from socketIO_client_nexus import SocketIO, LoggingNamespace
import json

viewData = json.dumps({'room': 1, 'view': "Calendar"})
print(viewData)
def on_connect():
    print('connect')


sio = SocketIO('192.168.2.9', 3000, LoggingNamespace)
sio.on('connect', on_connect)
sio.emit('changeView', viewData)
