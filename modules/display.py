# -*- coding: utf-8 -*-
#Imports
import grove_rgb_lcd as lcd
import grovepi
from time import sleep
import views.View as View
from sensor import getDhtData as getSensorData

#Sensors connected
button_port = 8
grovepi.pinMode(button_port,'INPUT')

#Views
thempHumView = View.TempView('', [150,50,100])
nofityView = View.NotifyView('No notifications', [120,0,0])

views = [thempHumView, nofityView]
currentView = 0

#Methods
def displayCurrentView ():
    try:
        views[currentView].display()
    except IndexError as e:
        print(e)
    
def turnOffDisplay ():
    lcd.setText('')
    lcd.setRGB(0,0,0)

def nextView():
    global currentView
    try:
        if(currentView == (len(views) - 1)):
            currentView = 0
            displayCurrentView()
        else:
            currentView += 1
            displayCurrentView()

    except IndexError as e:
        print(e)

def exitProgram():
    print('Closing program...')
    lcd.setText('Closing program...')
    sleep(3)
    turnOffDisplay()

  
#Listens to button events
while True:
    try:        
        if(grovepi.digitalRead(button_port)):
            print('single press')
            nextView()
            sleep(0.5)
        
    except KeyboardInterrupt:
        exitProgram()
        break
    
    except IOError:
        # Print "Error" if communication error encountered
        print ("Error")

