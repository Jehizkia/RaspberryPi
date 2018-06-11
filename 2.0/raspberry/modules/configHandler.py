#imports
import ConfigParser
import os
from time import sleep
import logging

savePath = '/home/pi/Desktop/rpiConfig.cfg'

config = ConfigParser.RawConfigParser()
configRead = ConfigParser.RawConfigParser()
configRead.read(savePath)

cfg_options = [{'section': 'app_data', 'field': 'room'},
                {'section': 'app_data', 'field': 'rpi_id'},
                {'section': 'app_data', 'field': 'api_url'},
                {'section': 'app_data', 'field': 'socket_url'},
                {'section': 'app_data', 'field': 'socket_port'},
                {'section': 'grovepi_data', 'field': 'button_port'},
                {'section': 'grovepi_data', 'field': 'rotaryangle_port'},
                {'section': 'grovepi_data', 'field': 'dht_sensor_port'},
                {'section': 'grovepi_data', 'field': 'dht_sensor_type'},
                {'section': 'grovepi_data', 'field': 'lcd_port'}               
                ]

cfg_default = [ {'section': 'app_data', 'field': 'rpi_id','value': 0 },
                {'section': 'app_data', 'field': 'api_url', 'value':'http://192.168.43.194:3000/'},
                {'section': 'app_data', 'field': 'socket_url', 'value': '192.168.2.14'},
                {'section': 'app_data', 'field': 'socket_port', 'value':'3000'},
                {'section': 'grovepi_data', 'field': 'button_port', 'value': 8},
                {'section': 'grovepi_data', 'field': 'rotaryangle_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_type', 'value':0},
                {'section': 'grovepi_data', 'field': 'lcd_port', 'value':0}               
                ]

cfg_manual = [  {'section': 'app_data', 'field': 'room'},
                {'section': 'app_data', 'field': 'rpi_id'},              
                ]

#init
def isFirstRun():
    if (configRead.has_section('app_data') == False or configRead.has_section('grovepi_data') == False):
        logging.info('First run')
        setup()
    else:
        logging.info('Not first run')

#set data
def setData(section,field, value):
    checkSection(section)
    config.set(section, field, value)

#check if sections exists
def checkSection(section):
    if config.has_section(section):
        logging.info('Exists: {}'.format(section))
    else:
        logging.info('Add section: {}'.format(section))
        config.add_section(section)
     
#Write
def writeToCfg():
    with open(savePath, 'wb') as configfile:
        config.write(configfile)
    logging.info('Config write finished')

def updateCfg():
    with open(savePath, 'wb') as configfile:
        configRead.write(configfile)
    logging.info('Config update finished')

#get data
def getData(section, value, value_type = ''):
    try:
        if('int' == value_type):
            return configRead.getint(section, value)
        elif('float' == value_type):
            return configRead.getfloat(section, value)
        elif('bool' == value_type):
            return configRead.getboolean(section, value)
        else:
            return configRead.get(section, value)
    except Exception as e:
        print ('Error {}: {}'.format(value,e))

def setup():
    print('Set up config file. \nChanges can always be made to data.cfg \nLocation: %s' % savePath)
    for option in cfg_options:
        userInput = raw_input('Enter {}: '.format(option['field']))
        setData(option['section'], option['field'], userInput)
        print(userInput)
    isNewRaspberry()
    writeToCfg()
    configRead.read(savePath)

def defaultSetup():
    print ('default config')
    
    userInput = raw_input('Enter room: ')
    setData('app_data', 'room', userInput)
    
    for option in cfg_default:
        setData(option['section'], option['field'], option['value'])

    isNewRaspberry()
    writeToCfg()
    configRead.read(savePath)


def configHasRequiredSections():
    if (configRead.has_section('app_data') == False or configRead.has_section('grovepi_data') == False):
        return False
    else:
        return True
    

def isNewRaspberry():
    userInput = raw_input('Has this raspberry been registered?[y/n]')
    if (userInput is 'y'):
        print 'yes'
        userInput = raw_input('Enter Raspberry ID: ')
        setData('app_data', 'rpi_id', userInput)
    elif(userInput is 'n'):
        print 'no'
        setData('app_data', 'rpi_id', 0)
    else:
        print ('Please enter y or n')

