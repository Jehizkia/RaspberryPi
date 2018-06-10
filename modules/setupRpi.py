import configHandler
import databaseHandler

def checkIfFirstRun():
    print ('Checking lmao')

#init
def isFirstRun():
    if (configHandler.configRead.has_section('app_data') == False or configHandler.configRead.has_section('grovepi_data') == False):
        print('-[Check]> First run')
        pickConfig()
    else:
        print('-[Check]> Not first run')

def pickConfig():
    userInput = raw_input('Use default configuration? [y/n]')
    if (userInput is 'y'):
        print 'yes'
        configHandler.defaultSetup()
        registerRoom()

    elif(userInput is 'n'):
        print 'no'
        configHandler.setup()
        registerRoom()
    else:
        print ('Please enter y or n')
        pickConfig()

def registerRoom():    
    #check if room exists
    rpiId = configHandler.getData('app_data', 'rpi_id')
    room = configHandler.getData('app_data', 'room')
    result = databaseHandler.getById('Raspberry', rpiId)
    if (len(result) > 0):
        databaseHandler.updateRaspberry(rpiId, room)
        print('Exists, update row with latests room')
        #update row with latests room
    else:
        print('Inserting')
        databaseHandler.insertRaspberry(room)
        newRpi = databaseHandler.getBy('Raspberry', 'room_code', room)
        print('Added to database')
        print newRpi
        configHandler.configRead.set('app_data', 'rpi_id', newRpi[0][0])
        configHandler.updateCfg()
        print('Config file updated')


#registerRoom()
#print (databaseHandler.getBy('Raspberry', 'room_code', 21)[0][1])
#isFirstRun()

