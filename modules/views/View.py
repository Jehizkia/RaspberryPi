from abc import ABCMeta, abstractmethod
from time import sleep
import grove_rgb_lcd as lcd
import sys
sys.path.append('../')
from sensor import getDhtData

class BaseView(object):
    __metaclass__ = ABCMeta

    def __init__(self, text, optional_color=[0,0,0]):
        self.text = text
        self.color = optional_color

    def setColor(self):
        lcd.setRGB(self.color[0],self.color[1], self.color[2])

    def updateText(self, text):
        self.text = text

    def display(self):
        lcd.setText(self.text)
        self.setColor()

class TempView(BaseView):
    def getTempHum(self):
        self.temperature = getDhtData()[0]
        self.humidity = getDhtData()[1]
        #call update text
        #call display

    def changeColorByTemp():
        pass

class NotifyView(BaseView):
    def getNotification(self):
        self.message = ''
    

x = TempView('testi333ng 1',[50,100,220])
x.display()
x.getTempHum()
print(x.temperature)





