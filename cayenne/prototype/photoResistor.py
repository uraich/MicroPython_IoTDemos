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
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

intensityChannel=1
illuminationLedChannel=2
indicatorLedChannel=3
# create adc and the led object
if sys.platform == "esp8266":
    print("photoResistor.py running on ESP8266")
    illuminationLed = Pin(16,Pin.OUT)
    adc = ADC(0)
else:
    print("photoResistor.py running on ESP32") 
    adc = ADC(Pin(36))
    illuminationLed = Pin(26,Pin.OUT)
    
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
