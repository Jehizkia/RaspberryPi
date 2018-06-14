from configHandler import DefaultSetup
from configHandler import ManualSetup
from configHandler import Configuration as config
from apiRequestController import ApiRequestController as api
import logging

logging.basicConfig(level=logging.INFO)

def isFirstRun():
    if (config().configHasRequiredSections()):
       logging.info('Skip setup')
    else: 
        pickConfig()

def pickConfig():
    userInput = raw_input('Use default configuration? [y/n]')
    if (userInput is 'y'):
        print 'You choose: Yes'
        #configHandler.defaultSetup()
        DefaultSetup().start()
        registerRoomOnServer()

    elif(userInput is 'n'):
        print 'You choose: No'
        #configHandler.setup()
        ManualSetup().start()
        registerRoomOnServer()
    else:
        print ('Please enter y or n')
        pickConfig()

def registerRoomOnServer():    
    rpiId = config().getData('app_data', 'rpi_id')
    roomCode = config().getData('app_data', 'room')
    if (ifRaspberryExists(rpiId)):
        api().postUpdateRaspberry(rpiId, roomCode)
        logging.info('Raspberry updated')
    else:
        logging.info('Inserting Raspberry into Database')
        api().postNewRaspberry(roomCode)
        updateConfigWithRpiId(roomCode)

def ifRaspberryExists(rpiId):
    rpi = api().getRaspberryByID(rpiId)
    if (len(rpi) > 0):
        return True
    else:
        return False

def updateConfigWithRpiId(roomCode):
    newRpi = api().getRoomByRoomCode(roomCode)
    config().configRead.set('app_data', 'rpi_id', newRpi[0]['id'])
    config().updateCfg()
    logging.info('Inserting Raspberry into Database')
