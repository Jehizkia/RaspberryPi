from configHandler import DefaultSetup
from configHandler import ManualSetup
from configHandler import Configuration
from apiRequestController import ApiRequestController
import logging

logging.basicConfig(level=logging.INFO)

class SetupRpi:

    def __init__(self):
        self.config = Configuration()
        self.api = None

    def isFirstRun(self):
        if (self.config.configHasRequiredSections()):
           logging.info('Skip setup')
        else: 
            self.pickConfig()

    def pickConfig(self):
        userInput = raw_input('Use default configuration? [y/n]')
        if (userInput is 'y'):
            print 'You choose: Yes'
            #configHandler.defaultSetup()
            DefaultSetup().start()
            self.registerRoomOnServer()

        elif(userInput is 'n'):
            print 'You choose: No'
            #configHandler.setup()
            ManualSetup().start()
            self.registerRoomOnServer()
        else:
            print ('Please enter y or n')
            self.pickConfig()

    def registerRoomOnServer(self):
        self.api = ApiRequestController()
        self.config = Configuration()
        rpiId = self.config.getData('app_data', 'rpi_id')
        roomCode = self.config.getData('app_data', 'room')
        if (self.ifRaspberryExists(rpiId)):
            self.api.postUpdateRaspberry(rpiId, roomCode)
            logging.info('Raspberry updated')
        else:
            logging.info('Inserting Raspberry into Database')
            self.api.postNewRaspberry(roomCode)
            self.updateConfigWithRpiId(roomCode)

    def ifRaspberryExists(self, rpiId):
        rpi = self.api.getRaspberryByID(rpiId)
        if (len(rpi) > 0):
            return True
        else:
            return False

    def updateConfigWithRpiId(self, roomCode):
        newRpi = self.api.getRoomByRoomCode(roomCode)
        self.config.configRead.set('app_data', 'rpi_id', newRpi[0]['id'])
        self.config.updateCfg()
        logging.info('Inserting Raspberry into Database')

