#
# cayenneBMP180.py
# Reads out the BMP180 barometric pressure and temperature sensor
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import I2C,Pin
from bmp180 import BMP180
import cayenne.client
import time

import logging



# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

bmp180TempChannel  = 12
bmp180PressChannel = 13

bus =  I2C(scl=Pin(5), sda=Pin(4), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

def senddata():
  bmp180.blocking_read()
  temp = bmp180.temperature
  p = bmp180.pressure
  altitude = bmp180.altitude
  print(temp, p, altitude)
  client.celsiusWrite(bmp180TempChannel,temp)
  time.sleep(1)
  client.hectoPascalWrite(bmp180PressChannel,p/100.0)
  time.sleep(4);
  
while True:
    try:
        senddata()
    except OSError:
        pass
