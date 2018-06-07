#imports
import ConfigParser
import os
from time import sleep

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

cfg_default = [{'section': 'app_data', 'field': 'room', 'value': 0},
                {'section': 'app_data', 'field': 'rpi_id','value': 0 },
                {'section': 'app_data', 'field': 'api_url', 'value':'http://192.168.43.194:3000/'},
                {'section': 'app_data', 'field': 'socket_url', 'value': '192.168.2.14'},
                {'section': 'app_data', 'field': 'socket_port', 'value':'3000'},
                {'section': 'grovepi_data', 'field': 'button_port', 'value': 8},
                {'section': 'grovepi_data', 'field': 'rotaryangle_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_type', 'value':0},
                {'section': 'grovepi_data', 'field': 'lcd_port', 'value':0}               
                ]

#init
def isFirstRun():
    if (configRead.has_section('app_data') == False or configRead.has_section('grovepi_data') == False):
        print('-[Check]> First run')
        setup()
    else:
        print('-[Check]> Not first run')

#set data
def setData(section,field, value):
    checkSection(section)
    config.set(section, field, value)
    print('-[Set cfg field]> Finished')

#check if sections exists
def checkSection(section):
    if config.has_section(section):
        print('-[field check]> %s Exists' % section)
    else:
        print('Section %s Not found' % section)
        config.add_section(section)
        print('-[Create cfg field]> Finished')
     
#Write
def writeToCfg():
    with open(savePath, 'wb') as configfile:
        config.write(configfile)
    print('-[Write cfg ]> Finished')

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

    writeToCfg()

def defaultSetup():
    print ('default config')
    userInput = raw_input('Enter room: ')
    setData('app_data', 'room', userInput)
    for option in cfg_default:
        setData(option['section'], option['field'], option['value'])
    writeToCfg()
    print(getData('grovepi_data', 'button_port', 'int'))
    print(getData('grovepi_data', 'rotaryangle_port', 'int'))
    print(getData('grovepi_data', 'button_port', 'int'))
    print(getData('grovepi_data', 'rotaryangle_port', 'int'))

    
    




