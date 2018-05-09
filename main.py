#Imports
import modules.groveController as controller
from time import sleep

#Main app

#init
def init():
    start()

#start
def start():
    
    #main loop
    while True:       
        controller.checkButtonPress()
        controller.checkRotaryTurn()
        sleep(0.5)
        
#stop
def stop():
    pass

init()
