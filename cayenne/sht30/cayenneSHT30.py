#
# cayenneSHT30.py
# Reads out the SHT30 temperature and humidity and sends the measurement
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import Pin
import cayenne.client
import sys,time
from sht30 import SHT30
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

sht30TempChannel = 5
sht30HumidityChannel = 6

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
# Check if SHT30 is connected
if not sht30.is_present():
    print("Could not find SHT30 board. Please connect it")
    sys.exit()
else:
    print("Found SHT-30, let's go on")
sht30.reset()

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
print("Successfully connected to myDevices MQTT broker")

def senddata():
  sht30Temperature, sht30Humidity = sht30.measure()
  print("Temperature: %6.3f"%sht30Temperature)
  client.celsiusWrite(sht30TempChannel,sht30Temperature)
  time.sleep(5)
  print("Relative humidity: %6.3f"%sht30Humidity + '%')
  client.humidityWrite(sht30HumidityChannel,sht30Humidity)
  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
