# -*- coding: utf-8 -*-
#Imports
import grove_rgb_lcd as lcd
import grovepi
from time import sleep
from views.Temp import TempView
from views.Notify import NotifyView

#Views
thempHumView = TempView('', [150,50,100])
nofityView = NotifyView('No notifications', [120,0,0])

views = [thempHumView, nofityView]
currentView = 0

#Methods
def displayCurrentView ():
    try:
        views[currentView].display()
        print('-[action]> Display current view')
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
            print('-[action]> Display next view')
        else:
            currentView += 1
            displayCurrentView()
            print('-[action]> Display next view')

    except IndexError as e:
        print(e)

def exitProgram():
    print('-[action]> Closing program')
    lcd.setText('Closing program...')
    sleep(1)
    turnOffDisplay()
