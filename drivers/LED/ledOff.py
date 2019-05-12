# ledOff.py: Switches the built-in LED off
# Both, ESP8266 and ESP32 use GPIO 2 to control the LED
# copyright: U. Raich, 12.5.2019
# This program was written as a demo for the AIS conference 2019, Kampala, Uganda
# released under GPL

from machine import Pin
import time

print("Switches the built-in LED off")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")
  
led = Pin(2,Pin.OUT)

led.off()



