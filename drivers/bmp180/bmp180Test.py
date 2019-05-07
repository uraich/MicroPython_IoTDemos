from bmp180 import BMP180
from machine import I2C, Pin                      # create an I2C bus object accordingly to the port you are using
import sys,time

# check on which board we are running
print("Testing the DS18B20 driver")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")
if sys.platform == "esp8266":
    print("Running on ESP8266")
    bus =  I2C(scl=Pin(5), sda=Pin(4), freq=100000)   # on esp8266
else:
    print("Running on ESP32") 
    bus = I2C(scl=Pin(22), sda=Pin(21), freq=100000)   # on esp32
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:
    bmp180.blocking_read()
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print(temp, p, altitude)
    time.sleep(2)
