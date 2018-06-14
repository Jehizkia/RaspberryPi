#imports
import ConfigParser
import logging

class Configuration:
    def __init__(self):
        self.savePath = '/home/pi/Desktop/rpiConfig.cfg'
        self.config = ConfigParser.RawConfigParser()
        self.configRead = ConfigParser.RawConfigParser()
        self.configRead.read(self.savePath)

    def setData(self, section, field, value):
        self.checkSection(section)
        self.config.set(section, field, value)

    def checkSection(self, section):
        if self.config.has_section(section):
            logging.info('Exists: {}'.format(section))
        else:
            logging.info('Add section: {}'.format(section))
            self.config.add_section(section)

    def writeToCfg(self):
        with open(self.savePath, 'wb') as configfile:
            self.config.write(configfile)
        logging.info('Config write finished')

    def updateCfg(self):
        with open(self.savePath, 'wb') as configfile:
            self.configRead.write(configfile)
        logging.info('Config update finished')

    def getData(self,section, value, value_type = ''):
        try:
            if('int' == value_type):
                return self.configRead.getint(section, value)
            elif('float' == value_type):
                return self.configRead.getfloat(section, value)
            elif('bool' == value_type):
                return self.configRead.getboolean(section, value)
            else:
                return self.configRead.get(section, value)
        except Exception as e:
            logging.error('Error {}: {}'.format(value,e))

    def isNewRaspberry(self):
        userInput = raw_input('Has this raspberry been registered?[y/n]')
        if (userInput is 'y'):
            print 'yes'
            userInput = raw_input('Enter Raspberry ID: ')
            self.setData('app_data', 'rpi_id', userInput)
        elif(userInput is 'n'):
            print 'no'
            self.setData('app_data', 'rpi_id', 0)
        else:
            print ('Please enter y or n')
            self.isNewRaspberry()

    def configHasRequiredSections(self):
        if (self.configRead.has_section('app_data') == False or self.configRead.has_section('grovepi_data') == False):
            return False
        else:
            return True

    def displayInfo(self):
        print ('Set up config file. \nChanges can always be made to data.cfg \nLocation: {}'.format(self.savePath))


class ManualSetup(Configuration):

    def __init__(self):
        Configuration.__init__(self)
        self.options = [{'section': 'app_data', 'field': 'room'},
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

    def start(self):
        self.displayInfo()
        for option in self.options:
            userInput = raw_input('Enter {}: '.format(option['field']))
            self.setData(option['section'], option['field'], userInput)
            print(userInput)
        self.isNewRaspberry()
        self.writeToCfg()
        self.configRead.read(self.savePath)
    

class DefaultSetup(Configuration):
    def __init__(self):
        Configuration.__init__(self)
        self.options = [ {'section': 'app_data', 'field': 'rpi_id','value': 0 },
                {'section': 'app_data', 'field': 'api_url', 'value':'http://192.168.2.4/api'},
                {'section': 'app_data', 'field': 'socket_url', 'value': '192.168.2.14'},
                {'section': 'app_data', 'field': 'socket_port', 'value':'3000'},
                {'section': 'grovepi_data', 'field': 'button_port', 'value': 8},
                {'section': 'grovepi_data', 'field': 'rotaryangle_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_port', 'value':2},
                {'section': 'grovepi_data', 'field': 'dht_sensor_type', 'value':0},
                {'section': 'grovepi_data', 'field': 'lcd_port', 'value':0}               
                ]
        
    def start(self):
        self.displayInfo()
        logging.info('default config')        
        userInput = raw_input('Enter room: ')
        self.setData('app_data', 'room', userInput)
        
        for option in self.options:
            self.setData(option['section'], option['field'], option['value'])

        self.isNewRaspberry()
        self.writeToCfg()
        self.configRead.read(self.savePath) 
