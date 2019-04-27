#
# cayenneDS18B20.py
# Reads out the DS18B20 1-wire digital thermometer and sends the measurement
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import Pin
import cayenne.client
import time
import onewire
import ds18x20
import logging

# the device is on GPIO 4
dat = Pin(4)
pinScl         =  5  #ESP8266 GPIO5 (D1)
pinSda         =  4  #ESP8266 GPIO4 (D2)

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

ds18b20Channel = 1

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))
# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

def senddata():
  ds.convert_temp()
  time.sleep_ms(100)
  temp = ds.read_temp(roms[0])
  print("Temperature: %f"%temp)
  client.celsiusWrite(ds18b20Channel,temp)
  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
