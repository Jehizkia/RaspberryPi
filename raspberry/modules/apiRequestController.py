from apiHandler import ApiRequest
import logging
import json

class ApiRequestController:

    def __init__(self):
        self.api = ApiRequest()
    
    def getRoomByRoomCode(self,roomCode):
        return self.parseJson(self.api.getData('/rpi/get/room/{}'.format(roomCode)))

    def getRaspberryByID(self, rpiID):
        return self.parseJson(self.api.getData('/rpi/get/raspberry/{}'.format(rpiID)))

    def getRaspberryByRoomCode(self, roomCode):
        return self.parseJson(self.api.getData('/rpi/get/room/{}/raspberry'.format(roomCode)))

    def getReservationByRoom(self, roomCode):
        return self.parseJson(self.api.getData('/rpi/get/reservation/{}'.format(roomCode)))

    def postSensorData(self, temperature, humidity, roomCode, timestamp):
        self.api.postData('/rpi/add/sensorData', {'temperature': temperature, 'humidity': humidity, 'room_code': roomCode, 'timestamp': timestamp})

    def postNewRaspberry(self, roomCode, active=1):
        self.api.postData('/rpi/add/raspberry',{'room_code':roomCode, 'active': active})

    def postUpdateRaspberry(self, id, roomCode):
         self.api.postData('/rpi/update/raspberry', {'room_code': roomCode, 'id': id})

    def parseJson(self, data):
        try:        
            return json.loads(data)['response']
        except:
            logging.error('An error as occured')
