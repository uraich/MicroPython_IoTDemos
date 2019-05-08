# sht30 test routine
# U. Raich 25.3.2019
from cayenne import Cayenne
from sht30 import SHT30
import sys,time

temperatureChannel=5
humidityChannel=6

cayenne=Cayenne()
cayenne.mqttConnect()

print("Successfully connected to myDevices MQTT broker")

def senddata():
  temperature, humidity = sht30.measure()
  dataString='temp,c=%6.3f'%temperature
  print("Publishing temperature: %s"%dataString)
  cayenne.publish(str(temperatureChannel),dataString)
  time.sleep(5)
  dataString='rel_hum,p=%6.3f'%humidity
  print("Publishing humidity: %s"%dataString)
  cayenne.publish(str(humidityChannel),dataString)
  time.sleep(5)

if sys.platform == "esp8266":
    print("Running on ESP8266")
    pinScl      =  5  #ESP8266 GPIO5 (D1
    pinSda      =  4  #ESP8266 GPIO4 (D2)
else:
    print("Running on ESP32") 
    pinScl      =  22  # SCL on esp32 
    pinSda      =  21  # SDA ON ESP32
    
# create SHT30 object
sht30=SHT30(scl_pin=pinScl, sda_pin=pinSda)

if not sht30.is_present():
    print("Could not find SHT30 board. Please connect it")
    sys.exit()
else:
    print("Found SHT-30, let's go on")

sht30.reset()
while True:
    try:
        senddata()
    except OSError:
        pass
