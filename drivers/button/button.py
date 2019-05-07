# button: reads the state of a button and prints it
# U.Raich 20.3.2019
# This prrogram was written for the workshop of IoT at the
# AIS conference 2019, Kampala, Uganda
# It is released under GPL

from machine import Pin
import sys,time

print("Testing the push button")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    button = Pin(0,Pin.IN,Pin.PULL_UP)
else:
    print("Running on ESP32") 
    button = Pin(17,Pin.IN,Pin.PULL_UP)

msg="not pressed"
len
while True:
    value = button.value()
    if value == 0:
        print("The switch is pressed    ")
    else:
        print("The switch is not pressed")
    time.sleep(1)    

 


