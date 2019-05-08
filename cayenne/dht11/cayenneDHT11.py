#
# cayenneDHT11.py
# Reads out the DHT11 temperature and humidity and sends the measurement
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import Pin
import cayenne.client
import time,sys
import dht
import logging

# create the dht11 object
if sys.platform == "esp8266":
    print("cayenneDHT11 running on ESP8266")
    dht11 = dht.DHT11(Pin(2))
else:
    print("cayenneDHT11 running on ESP32") 
    dht11 = dht.DHT11(Pin(16))

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

dht11TempChannel = 7
dht11HumidityChannel = 8

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
print("Successfully connected to myDevices MQTT broker")
def senddata():
  print("Measuring...")
  dht11.measure()
  temp = dht11.temperature()
  print("Temperature: %f °C"%temp)
  client.celsiusWrite(dht11TempChannel,temp)
  time.sleep(5)
  humidity=dht11.humidity()
  print("Relative humidity: %6.3f"%humidity + '%')
  client.humidityWrite(dht11HumidityChannel,humidity)
  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
