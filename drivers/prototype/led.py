from machine import Pin
import time,sys

print("Testing the led on the prototype board")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    led=Pin(16,Pin.OUT)

else:
    print("Running on ESP32") 
    led=Pin(26,Pin.OUT)

while True:
  led.value(1)
  time.sleep(0.5)
  led.value(0)
  time.sleep(0.5)


