#
# cayenneButton.py
# Reads out the state of a push button and sends the result
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import Pin
import cayenne.client
import time,time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

buttonChannel = 10
if sys.platform == "esp8266":
    print("cayenneButton running on ESP8266")
    button = Pin(0,Pin.IN,Pin.PULL_UP)
else:
    print("cayenneButton running on ESP32") 
    button = Pin(17,Pin.IN,Pin.PULL_UP)

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

def senddata():
  pbValue=button.value()
  # button is active low
  if (pbValue):
      client.digitalWrite(buttonChannel,0)
  else:
      client.digitalWrite(buttonChannel,1)

  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
