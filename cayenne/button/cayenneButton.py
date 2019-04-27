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
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "7c70a330-69af-11e8-a76a-fdebb8d0010d"
MQTT_PASSWORD  = "32d184add41570759dd1735fa464cef7e62876a4"
MQTT_CLIENT_ID = "dae86710-4ae9-11e9-a6b5-e30ec853fbf2"

buttonChannel = 10
button=Pin(0,Pin.IN,pull=Pin.PULL_UP) # Declaring button on GPIO 0

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

def senddata():
  pbValue=button.value()

  client.digitalWrite(buttonChannel,pbValue)
  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
