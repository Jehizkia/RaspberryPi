#imports
import ConfigParser

config = ConfigParser.RawConfigParser()

configRead = ConfigParser.RawConfigParser()
configRead.read('../data.cfg')

#init
def isFirstRun(): 
    if (configRead.has_section('app_data') == False and configRead.has_section('grovepi_data') == False):
        print('is first run')
    else:
        print('not first run')

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
    with open('../data.cfg', 'wb') as configfile:
        config.write(configfile)
    print('-[Write cfg ]> Finished')

#get data
def getData(section, value, value_type = ''):
    if('int' == value_type):
        return configRead.getint(section, value)
    else:
        return configRead.get(section, value)

setData('app_data','room', 'h412')
setData('app_data','rpi_id', '1')
setData('app_data','api_url', 'http://192.168.43.194:3000/')
setData('app_data','socket_url', '192.168.43.194')
setData('app_data','socket_port', '3000')

setData('grovepi_data','button_port', '1')
setData('grovepi_data','rotaryangle_port', '1')
setData('grovepi_data','dht_sensor_port', '1')
setData('grovepi_data','lcd_port', '1')

writeToCfg()




