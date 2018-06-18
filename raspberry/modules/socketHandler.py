from socketIO_client_nexus import SocketIO, LoggingNamespace
import json
import os, sys
import logging
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from configHandler import Configuration as config

class SocketWriter:

    def __init__(self):
        self._url = config().getData('app_data', 'socket_url')
        self._port = config().getData('app_data', 'socket_port', 'int')
        logging.info('-[request]>connecting')
        try:
            self._socket = SocketIO(self._url,self._port, wait_for_connection=False)
        except:
            logging.error('-[request failed]>Socket server is down.')

    def send(self, event, data):
        jsonData = json.dumps(data)
        try:
            self._socket.emit(event,jsonData)
        except:
            logging.error('-[request failed]>Socket server is down.')
