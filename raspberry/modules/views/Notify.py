#imports
from View import BaseView
import grove_rgb_lcd as lcd

class NotifyView(BaseView):
    def getNotification(self):
        self.message = ''

    def display(self):
        lcd.setText(self.text)
        self.setColor()
