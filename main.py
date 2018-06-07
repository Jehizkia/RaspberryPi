#Setup
from modules.setupRpi import isFirstRun
isFirstRun()

#Imports
import sys
import modules.groveController as controller
from time import sleep
from modules.display import turnOffDisplay

#Main app
print('run')
#init
def init():
    print('-[init]initialization')    
    controller.init()
    start()

#start
def start():
    print('-[start] Program has started')
    
    #main loop
    while True:
        try:
            controller.check()
            sleep(0.5)
        except KeyboardInterrupt:            
            stop()
    
#stop
def stop():
    print('-[action]> Exiting program')
    turnOffDisplay()
    sys.exit(1)

init()

