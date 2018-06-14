import apiHandler as api
import configHandler as config
import logging
import time
import json

def getRoomByRoomCode(roomCode):
    return parseJson(api.getData('/rpi/get/room/{}'.format(roomCode)))

def getRaspberryByID(rpiID):
    return parseJson(api.getData('/rpi/get/raspberry/{}'.format(rpiID)))

def getRaspberryByRoomCode(roomCode):
    return parseJson(api.getData('/rpi/get/room/{}/raspberry'.format(roomCode)))

def getReservationByRoom(roomCode):
    return parseJson(api.getData('/rpi/get/reservation/{}'.format(roomCode)))

def postSensorData(temperature, humidity, roomCode, timestamp):
    api.postData('/rpi/add/sensorData', {'temperature': temperature, 'humidity': humidity, 'room_code': roomCode, 'timestamp': timestamp})

def postNewRaspberry(roomCode, active=1):
    api.postData('/rpi/add/raspberry',{'room_code':roomCode, 'active': active})

def postUpdateRaspberry(id, roomCode):
     api.postData('/rpi/update/raspberry', {'room_code': roomCode, 'id': id})


def parseJson(data):
    try:        
        return json.loads(data)['response']
    except:
        logging.error('An error as occured')
