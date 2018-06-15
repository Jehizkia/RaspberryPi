#import
import grove_rgb_lcd as lcd
from View import BaseView 
import sys,os
sys.path.insert(1, os.path.join(sys.path[0], './modules'))
#import sensor
#sys.path.append('/home/pi/Desktop/ictlab/rpiGit/RaspberryPi/modules')
from sensor import Sensor


class TempView(BaseView):
    
    def getTempHum(self):
        self.temperature = Sensor().getDhtData()[0]
        self.humidity = Sensor().getDhtData()[1]
        self.updateText('Temp:' + str(self.temperature) + 'C\nHum:' + str(self.humidity))
    
    def display(self):
        self.getTempHum()
        lcd.setText(self.text)
        self.setColor()
