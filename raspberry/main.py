#Setup
from modules.setupRpi import isFirstRun
isFirstRun()

#Imports
import sys, logging
from modules.groveController import GroveController
from time import sleep
from modules.display import DisplayController

logging.basicConfig(level=logging.INFO)
controller = GroveController()

def start():
    logging.info('Start app')     
    #main loop
    while True:
        try:
            controller.check()
            sleep(0.5)
        except KeyboardInterrupt:            
            stop()
    
def stop():
    logging.info('Exiting program')
    DisplayController().turnOffDisplay()
    sys.exit(1)

if __name__=='__main__':
    start()
