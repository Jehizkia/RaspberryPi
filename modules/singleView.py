import grove_rgb_lcd as lcd
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

    def updateText(self, text):
        self.text = text
