from grovepi import *
from time import sleep
from math import isnan
from configHandler import Configuration

class Sensor:

    def __init__(self):
        self.config = Configuration()
        self.sensor_port = self.config.getData('grovepi_data', 'dht_sensor_port', 'int')
        self.sensor_type = self.config.getData('grovepi_data', 'dht_sensor_type', 'int')

    def getDhtData(self):
        try:
            #DHT sensor module
            data = dht(self.sensor_port, self.sensor_type)
            #if we have nans
            if isnan(data[0]) is True or isnan(data[1]) is True:
                #raise TypeError('nan error')
                self.getDhtData()

            if data is not None or isnan(data[0]) is True  or isnan(data[1]) is True :
                return data

            else:
                 self.getDhtData()
                
        except KeyboardInterrupt as e:
            print('Exit program')
