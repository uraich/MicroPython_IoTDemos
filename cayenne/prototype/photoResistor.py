#
# photoResistor.py
# Reads out the photo resistor via the ESP8266 ADC and sends the values
# to Cayenne
# Switches on and of the LED so see differences
# copyright U. Raich
# This is a demo program for a talk on IoT at the African Internet Summit 2019
# Released under GPL
#
from machine import Pin,ADC
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "7c70a330-69af-11e8-a76a-fdebb8d0010d"
MQTT_PASSWORD  = "32d184add41570759dd1735fa464cef7e62876a4"
MQTT_CLIENT_ID = "d6accfc0-6541-11e9-bdb5-dfd20f02ea3f"

intensityChannel=1
illuminationLedChannel=2
indicatorLedChannel=3
# create adc and the led object
adc = ADC(0)
illuminationLed = Pin(16,Pin.OUT)
count=0
ledValue=0
# switch LED off
illuminationLed.value(ledValue)

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)

while True:
    client.loop()
    lightIntensity = adc.read()
    print("Light intensity value from ADC: %d"%lightIntensity);
    print("Count: %d"%count)
    print("led value: %d"%ledValue)
    
    client.voltageWrite(intensityChannel, lightIntensity)
    time.sleep(1)
    count += 1
    if count > 5:
        if ledValue == 0:
            ledValue = 1
        else:
            ledValue = 0
        illuminationLed.value(ledValue)
        count = 0
