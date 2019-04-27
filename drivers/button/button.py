# button: reads the state of a button and prints it
# U.Raich 20.3.2019
# This prrogram was written for the workshop of IoT at the
# AIS conference 2019, Kampala, Uganda
# It is released under GPL

from machine import Pin
import time

button = Pin(0,Pin.IN,Pin.PULL_UP)

while True:
    value = button.value()
    if value == 0:
        print("The switch is pressed    ",end='\r',flush=True)
    else:
        print("The switch is not pressed",end='\r',flush=True)
    time.sleep(1)    
    


