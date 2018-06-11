import grovepi
import display
import socketHandler
import configHandler as config
import databaseHandler
import sensor
import time

#Ports/settings
button_port = config.getData('grovepi_data', 'button_port', 'int')
rotary_port = config.getData('grovepi_data', 'rotaryangle_port', 'int')

rpiId = config.getData('app_data', 'rpi_id', 'int')
roomCode = config.getData('app_data', 'room')

grovepi.pinMode(button_port, 'INPUT')

#globals
current = 0
refreshCount = 0
refreshRate = 5
socket = socketHandler.SocketWriter()

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
        if( ifCurrentView(current, 1)):
             pass
        else:          
             print('-[action]> Rotary view: 1')
             socket.send('changeView', {'room': 1, 'view':'Calendar'})
        current = 1
        
    elif (rotaryPosistion >= 341 and rotaryPosistion <= 682):
        if( ifCurrentView(current, 2)):
            pass
        else:
            print('-[action]> Rotary view: 2')
            socket.send('changeView', {'room': 1, 'view':'Temperature'})
        current = 2
    else:
        if( ifCurrentView(current, 3)):
            pass
        else:
            print('-[action]> Rotary view: 3')
            socket.send('changeView', {'room': 1, 'view':'Room changes'})
        current = 3

#Check if current view equals rotaryView
def ifCurrentView(current, rotaryView):
    if(rotaryView is not current):
        return False
    else:
        return True

def checkRefresh():
   global refreshCount, refreshRate
   if(refreshCount >= refreshRate):
      refreshCount = 0
      display.displayCurrentView()
      databaseHandler.insertTempHum(sensor.getDhtData()[0],  sensor.getDhtData()[1], roomCode, time.time())
   else:
      refreshCount+= 1

def check():
   checkButtonPress()
   checkRotaryTurn()
   checkRefresh()
