#imports
import ConfigParser
import os

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
                {'section': 'grovepi_data', 'field': 'lcd_port'}               
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
    if('int' == value_type):
        return configRead.getint(section, value)
    else:
        return configRead.get(section, value)

def setup():
    print('Set up config file. \nChanges can always be made to data.cfg \nLocation: %s' % savePath)
    for option in cfg_options:
        userInput = raw_input('Enter %s: ' % option['field'])
        setData(option['section'], option['field'], userInput)
        print(userInput)

    writeToCfg()

#isFirstRun()




