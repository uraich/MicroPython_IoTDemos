# sht30 test routine
# U. Raich 25.3.2019

from sht30 import SHT30
import sys,time

print("Testing the SHT30 temperature and humidity sensor")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")
if sys.platform == "esp8266":
    print("Running on ESP8266")
    pinScl      =  5  #ESP8266 GPIO5 (D1
    pinSda      =  4  #ESP8266 GPIO4 (D2)
else:
    print("Running on ESP32") 
    pinScl      =  22  # SCL on esp32 
    pinSda      =  21  # SDA ON ESP32

sht30=SHT30(scl_pin=pinScl, sda_pin=pinSda)
if not sht30.is_present():
    print("Could not find SHT30 board. Please connect it")
    sys.exit()
else:
    print("Found SHT-30, let's go on")

sht30.reset()
while True:
    temperature, humidity = sht30.measure()
    print('Temperature',temperature,'°C, RH:',humidity,' %')
    time.sleep(2)