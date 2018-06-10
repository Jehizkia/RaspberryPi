#Imports
import grove_rgb_lcd as lcd
import grovepi
from viewController import RequestController, Request
from time import sleep

viewControl = RequestController()
viewRequests = ['temp', 'notify']
currentView = 0

#Methods
def displayCurrentView ():
    try:
        viewControl.dispatch_request(Request(viewRequests[currentView]))
        print('-[action]> Display current view')
    except IndexError as e:
        print(e)
    
def turnOffDisplay ():
    lcd.setText('')
    lcd.setRGB(0,0,0)

def nextView():
    global currentView
    try:
        if(currentView == (len(viewRequests) - 1)):
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
