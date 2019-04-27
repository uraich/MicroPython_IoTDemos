#
# ledControl.py
# There are 2 LEDS on the prototype system: One on the prototype card to
# illuminate the photo resistor and the built-in LED on the CPU card
# 2 buttons on Cayenne allow to switch these LEDs on and off
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

global intensityChannel
global illuminationLedChannel
global indicatorLedChannel
global illuminationLed,indicatorLed
intensityChannel = 1
illuminationLedChannel=2
indicatorLedChannel=3
illuminationLed = Pin(16,Pin.OUT)
indicatorLed = Pin(2,Pin.OUT)

# callback routine to treat command messages from Cayenne
def on_message(message):
    global illuminationLedChannel,indicatorLedChannel
    msg = cayenne.client.CayenneMessage(message[0],message[1])
    if msg.channel == indicatorLedChannel:
        if int(msg.value) == 1:
            indicatorLed.value(0)
        else:
            indicatorLed.value(1)
        if int(msg.value) == 1:
            print("Switching indicator led on");
        else:
            print("Switching indicator led off");
    elif msg.channel == illuminationLedChannel:
        if int(msg.value) == 1:
            print("Switching illumination led on");
        else:
            print("Switching illumination led off");
        illuminationLed.value(int(msg.value))
    return

# create adc and the led object
adc = ADC(0)
count=0
ledValue=0
# switch LED off
illuminationLed.value(0)             # active high
indicatorLed.value(1)                # active low

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# register callback
client.on_message=on_message
timestamp = 0

while True:
    client.loop()
    lightIntensity = adc.read()
    print("Light intensity value from ADC: %d"%lightIntensity);
    client.voltageWrite(intensityChannel, lightIntensity)
    time.sleep(1)

