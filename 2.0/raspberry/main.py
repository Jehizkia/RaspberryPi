#Setup
from modules.setupRpi import isFirstRun
isFirstRun()

#Imports
import sys, logging
import modules.groveController as controller
from time import sleep
from modules.display import turnOffDisplay

logging.basicConfig(level=logging.INFO)

def init():
    logging.info('Initialization')
    controller.init()
    start()

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
    turnOffDisplay()
    sys.exit(1)

init()

