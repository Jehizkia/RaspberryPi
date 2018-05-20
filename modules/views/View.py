from abc import ABCMeta, abstractmethod
from time import sleep
import grove_rgb_lcd as lcd

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
   


