import grovepi
from display import DisplayController as displayControl
import socketHandler
from apiRequestController import ApiRequestController
from configHandler import Configuration as config
from sensor import Sensor
import time

class GroveController:

   def __init__(self):
      #Ports/RPI settings
      self.button_port = config().getData('grovepi_data', 'button_port', 'int')
      self.rotary_port = config().getData('grovepi_data', 'rotaryangle_port', 'int')
      self.rpiId = config().getData('app_data', 'rpi_id', 'int')
      self.roomCode = config().getData('app_data', 'room')
      self.display = displayControl()
      grovepi.pinMode(self.button_port, 'INPUT')

      self.current = 0
      self.refreshCount = 0
      self.refreshRate = 10
      self.socket = socketHandler.SocketWriter()
      self.api = ApiRequestController()
      self.sensor = Sensor()

      self.display.displayCurrentView()

   def checkButtonPress(self):
       if(grovepi.digitalRead(self.button_port)):
           print('-[action]> Single button press')
           self.display.nextView()

   def checkRotaryTurn(self):      
       rotaryPosistion = grovepi.analogRead(self.rotary_port)

       #if rotaryPosition is in range execute a function once
       if (rotaryPosistion >= 682 and rotaryPosistion <= 1023):                
           if( self.ifCurrentView(self.current, 1)):
                pass
           else:          
                print('-[action]> Rotary view: 1')
                self.socket.send('changeView', {'room': 1, 'view':'Calendar'})
           self.current = 1
           
       elif (rotaryPosistion >= 341 and rotaryPosistion <= 682):
           if( self.ifCurrentView(self.current, 2)):
               pass
           else:
               print('-[action]> Rotary view: 2')
               self.socket.send('changeView', {'room': 1, 'view':'Temperature'})
           self.current = 2
       else:
           if(self.ifCurrentView(self.current, 3)):
               pass
           else:
               print('-[action]> Rotary view: 3')
               self.socket.send('changeView', {'room': 1, 'view':'Room changes'})
           self.current = 3

   #Check if current view equals rotaryView
   def ifCurrentView(self,current, rotaryView):
       if(rotaryView is not current):
           return False
       else:
           return True

   def checkRefresh(self):
      if(self.refreshCount >= self.refreshRate):
         self.refreshCount = 0
         self.display.displayCurrentView()
         self.api.postSensorData(self.sensor.getDhtData()[0],  self.sensor.getDhtData()[1], self.roomCode, time.time())      
      else:
         self.refreshCount+= 1

   def check(self):
      self.checkButtonPress()
      self.checkRotaryTurn()
      self.checkRefresh()
         
