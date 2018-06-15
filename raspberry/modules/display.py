#Imports
import grove_rgb_lcd as lcd
import grovepi
from viewController import RequestController, Request
from time import sleep

class DisplayController:

    def __init__(self):
        self.viewControl = RequestController()
        self.viewRequests = ['temp', 'notify']
        self.currentView = 0
    
    def displayCurrentView (self):
        try:
            self.viewControl.dispatch_request(Request(self.viewRequests[self.currentView]))
            print('-[action]> Display current view')
        except IndexError as e:
            print(e)
        
    def turnOffDisplay (self):
        lcd.setText('')
        lcd.setRGB(0,0,0)

    def nextView(self):
        self.currentView
        try:
            if(self.currentView == (len(self.viewRequests) - 1)):
                self.currentView = 0
                self.displayCurrentView()
                print('-[action]> Display next view')
            else:
                self.currentView += 1
                self.displayCurrentView()
                print('-[action]> Display next view')

        except IndexError as e:
            print(e)

    def exitProgram(self):
        print('-[action]> Closing program')
        lcd.setText('Closing program...')
        sleep(1)
        self.turnOffDisplay()
