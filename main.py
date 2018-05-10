#Imports
import modules.groveController as controller
from time import sleep

#Main app
print('run')
#init
def init():
    print('-[init]initialization')
    start()

#start
def start():
    print('-[action] Program has started')
    
    #main loop
    while True:       
        controller.checkButtonPress()
        controller.checkRotaryTurn()
        sleep(0.5)
        
#stop
def stop():
    pass

init()

