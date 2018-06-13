import apiHandler
import configHandler as config
import logging
import time
import json

def getRoomByRoomCode(roomCode):
    return parseJson(apiHandler.getData('/rpi/get/room/{}'.format(roomCode)))

def getRaspberryByID(rpiID):
    return parseJson(apiHandler.getData('/rpi/get/raspberry/{}'.format(rpiID)))

def getReservationByRoom(roomCode):
    return parseJson(apiHandler.getData('/rpi/get/reservation/{}'.format(roomCode)))

def postSensorData(data):
    apiHandler.postData('/rpi/add/sensorData', data)

def postNewRaspberry(data):
    pass

def postUpdateRaspberry(data):
    pass


def parseJson(data):
    try:        
        return json.loads(data)['response']
    except:
        logging.error('An error as occured')

