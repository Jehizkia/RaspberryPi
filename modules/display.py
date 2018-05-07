# -*- coding: utf-8 -*-
#Imports
import grove_rgb_lcd as lcd
import grovepi
from time import sleep
from singleView import View
from sensor import getDhtData as getSensorData

#Sensors connected
button_port = 8
grovepi.pinMode(button_port,'INPUT')

#Views
view1Text = 'Temp:' + str(getSensorData()[0]) + 'C\nHum:' + str(getSensorData()[1])
view1 = View(1, view1Text , [0,0,225])
view2 = View(2, 'Notifier\nNo messages...', [225,0,0])
view3 = View(3, 'vuejs ;)', [0,255,0])

currentView = 0
views = [view1, view2, view3]

#Methods
def displayCurrentView ():
    try:
        lcd.setText(views[currentView].text)
        views[currentView].setColor()
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
            refreshViews()
        else:
            currentView += 1
            displayCurrentView()
            refreshViews()

    except IndexError as e:
        print(e)

def refreshViews():
    global view1
    view1.updateText(view1Text)
    print('updating')
    print(getSensorData())
def exitProgram():
    print('Closing program...')
    lcd.setText('Closing program...')
    sleep(3)
    turnOffDisplay()

  
#Listens to button events
while True:
    try:        
        if(grovepi.digitalRead(button_port)):
            print('button press')
            nextView()
            sleep(0.5)
    except KeyboardInterrupt:
        exitProgram()
        break
    
    except IOError:				# Print "Error" if communication error encountered
        print ("Error")

