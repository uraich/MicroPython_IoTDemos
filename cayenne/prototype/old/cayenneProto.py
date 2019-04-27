from machine import Pin,ADC
from cayenne import Cayenne
import network
import time

# the illumination LED is on GPIO 16
# the built-in LED on GPIO 2
# the photo-resistor on ADC A0

addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display height in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False
cayenneChannel=1
# Cayenne definitions
CLIENT_ID="d6accfc0-6541-11e9-bdb5-dfd20f02ea3f"

intensityChannel=1
illuminationLedChannel=2
indicatorLedChannel=3

# create adc and the led object
adc = ADC(0)
illuminationLed = Pin(16,Pin.OUT)
global count,ledValue
count=0
ledValue=0
# switch LED off
illuminationLed.value(ledValue)

cayenne=Cayenne(CLIENT_ID)
cayenne.mqttConnect()

print("Successfully connected to myDevices MQTT broker")
def senddata():
  global count,ledValue
  lightIntensity = adc.read()
  print("Light intensity value from ADC: %d"%lightIntensity);
  print("Count: %d"%count)
  print("led value: %d"%ledValue)
  intensityString = "voltage,mv=%d"%lightIntensity
  cayenne.publish(str(intensityChannel),intensityString)
  time.sleep(2)
  count+=1
  if count > 2:
    if ledValue == 0:
      ledValue = 1
    else:
      ledValue = 0;
    illuminationLed.value(ledValue)
    count = 0

while True:
    try:
        senddata()
    except OSError:
        pass



