import configHandler
import databaseHandler
import logging

def isFirstRun():
    if (configHandler.configHasRequiredSections()):
        print('Skip setup')
    else: 
        pickConfig()

def pickConfig():
    userInput = raw_input('Use default configuration? [y/n]')
    if (userInput is 'y'):
        print 'You choose: Yes'
        configHandler.defaultSetup()
        registerRoomOnServer()

    elif(userInput is 'n'):
        print 'You choose: No'
        configHandler.setup()
        registerRoomOnServer()
    else:
        print ('Please enter y or n')
        pickConfig()

def registerRoomOnServer():    
    #check if room exists
    rpiId = configHandler.getData('app_data', 'rpi_id')
    roomCode = configHandler.getData('app_data', 'room')
    
    if (ifRaspberryExists(rpiId)):
        databaseHandler.updateRaspberry(rpiId, roomCode)
        logging.info('Raspberry updated')
    else:
        logging.info('Inserting Raspberry into Database')
        databaseHandler.insertRaspberry(roomCode)
        updateConfigWithRpiId(roomCode)

def ifRaspberryExists(rpiId):
    rpi = databaseHandler.getById('Raspberry', rpiId)
    if (len(rpi) > 0):
        return True
    else:
        return False

def updateConfigWithRpiId(roomCode):
    newRpi = databaseHandler.getBy('Raspberry', 'room_code', roomCode)
    #Adding id of the new Rpi to config
    configHandler.configRead.set('app_data', 'rpi_id', newRpi[0][0])
    configHandler.updateCfg()
    logging.info('Inserting Raspberry into Database')
    
