import grovepi
import display
import socketHandler as rpisocket
import configHandler as config

#print config.getData('grovepi_data', 'button_port', 'int')
#Ports/settings
button_port = config.getData('grovepi_data', 'button_port', 'int')
rotary_port = config.getData('grovepi_data', 'rotaryangle_port', 'int')

grovepi.pinMode(button_port, 'INPUT')

#globals
current = 0

def init():
   display.displayCurrentView()

def checkButtonPress():
    if(grovepi.digitalRead(button_port)):
        print('-[action]> Single button press')
        display.nextView()

#checks current posistion of rotary
def checkRotaryTurn():
    global current
   
    rotaryPosistion = grovepi.analogRead(rotary_port)

    #if rotaryPosition is in range execute a function once
    if (rotaryPosistion >= 682 and rotaryPosistion <= 1023):                
        if( checkIfCurrent(current, 1)):
             pass
        else:          
             print('-[action]> Rotary view: 1')
             rpisocket.changeView(1,'Calendar')
        current = 1
        
    elif (rotaryPosistion >= 341 and rotaryPosistion <= 682):
        if( checkIfCurrent(current, 2)):
            pass
        else:
            print('-[action]> Rotary view: 2')
            rpisocket.changeView(1,'Temperature')
        current = 2
    else:
        if( checkIfCurrent(current, 3)):
            pass
        else:
            print('-[action]> Rotary view: 3')
            rpisocket.changeView(1,'Room changes')
        current = 3

#Check if current view equals rotaryView
def checkIfCurrent(current, rotaryView):
    if(rotaryView is not current):
        return False
    else:
        return True


