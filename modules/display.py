#Imports
import grove_rgb_lcd as lcd
import grovepi
from time import sleep

#Sensors connected
button_port = 8
grovepi.pinMode(button_port,'INPUT')

#View class
class View:
    def __init__(self, viewID, text, optional_color=[0,0,0]):
        self.viewID = viewID
        self.text = text
        self.color = optional_color

    #Sets backgroundcolor
    def setColor(self):
        lcd.setRGB(self.color[0],self.color[1], self.color[2])

    def refreshView(self):
        lcd.setText(self.text)
        setColor()        

#Views
view1 = View(1, 'Temperature', [0,0,225])
view2 = View(2, 'Notifications', [225,0,0])
view3 = View(3, 'vuejs is bae', [0,255,0])

currentView = 0
views = [view1, view2, view3]

## Methods

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
    print(currentView)
    try:
        if(currentView == (len(views) - 1)):
            print('reset')
            currentView = 0
            displayCurrentView()
        else:
            print('increment')
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
            print('button press')
            nextView()
            sleep(0.1)
    except KeyboardInterrupt:
        exitProgram()
        break
    
    except IOError:				# Print "Error" if communication error encountered
        print ("Error")

