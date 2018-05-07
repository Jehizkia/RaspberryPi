#Imports
import grove_rgb_lcd as lcd
from time import sleep

#Dislay sensor data

def TempHum ():
    print('Displaying data')
    lcd.setText('')
    sleep(2)
    lcd.setText('Loading \ndepression.')
    lcd.setRGB(52,152,219)
    sleep(1)
    lcd.setText_norefresh('Loading \ndepression..')
    sleep(1)
    lcd.setText_norefresh('Loading \ndepression...')
    sleep(1)
    lcd.setText_norefresh('Loading \ndepression.')
    sleep(1)    
    lcd.setText('Depression 100% \nloaded!')
    lcd.setRGB(46,204,113)
    sleep(3)
    lcd.setText('Ouassim is ready \nfor the day :D')
    sleep(5)
    lcd.setRGB(0,0,0)
    lcd.setText('')

TempHum()
