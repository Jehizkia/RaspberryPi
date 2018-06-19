from abc import ABCMeta, abstractmethod
from time import sleep
import grove_rgb_lcd as lcd
from sensor import Sensor

class BaseView(object):
    __metaclass__ = ABCMeta

    def __init__(self, text, optional_color=[0,0,0]):
        self.text = text
        self.color = optional_color

    def setColor(self):
        lcd.setRGB(self.color[0],self.color[1], self.color[2])

    def updateText(self, text):
        self.text = text

    def clearScreen(self):
        lcd.setText('')

    @abstractmethod
    def display(self):
        pass
   
class NotifyView(BaseView):
    def getNotification(self):
        self.message = ''

    def display(self):
        lcd.setText(self.text)
        self.setColor()

class TempView(BaseView):
    
    def getTempHum(self):
        self.temperature = Sensor().getDhtData()[0]
        self.humidity = Sensor().getDhtData()[1]
        self.updateText('Temp:' + str(self.temperature) + 'C\nHum:' + str(self.humidity))
    
    def display(self):
        self.getTempHum()
        lcd.setText(self.text)
        self.setColor()
