from grovepi import *
from time import sleep
from math import isnan
import configHandler as config

sensor_port = config.getData('grovepi_data', 'dht_sensor_port', 'int')
sensor_type = config.getData('grovepi_data', 'dht_sensor_type', 'int')

def getDhtData():
    try:
        #DHT sensor module
        data = dht(sensor_port,sensor_type)
        #if we have nans
        if isnan(data[0]) is True or isnan(data[1]) is True:
            #raise TypeError('nan error')
            getDhtData()

        if data is not None or isnan(data[0]) is True  or isnan(data[1]) is True :
            return data

        else:
             getDhtData()
            
    except KeyboardInterrupt as e:
        print('Exit program')     

    

