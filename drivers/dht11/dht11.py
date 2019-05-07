import dht
from machine import Pin
import sys,time

print("Testing the dht11 temperature and humidity sensor")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    d = dht.DHT11(Pin(2))
else:
    print("Running on ESP32") 
    d = dht.DHT11(Pin(16))

while True:
    d.measure()
    temp=d.temperature()
    hum=d.humidity()

    print("Temperature: %d"%temp)
    print("Humidity: %d"%hum)
    time.sleep(2)
