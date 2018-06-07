import configHandler

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

    elif(userInput is 'n'):
        print 'no'
        configHandler.setup()
    else:
        print ('Please enter y or n')
        pickConfig()

def registerRoomOnDB():
    pass

